# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import timedelta


class TodoList(models.Model):
    _name = 'mail.activity'
    _inherit = ['mail.activity', 'mail.thread']
    _rec_name = 'summary'

    date_deadline = fields.Date('Due Date', index=True, required=True, default=fields.Date.context_today, store=True)
    user_id = fields.Many2one('res.users', string='User', index=True, tracking=True, default=lambda self: self.env.user)
    res_model_id = fields.Many2one('ir.model', 'Document Model', index=True, ondelete='cascade', required=True)
    res_id = fields.Many2oneReference(string='Related Document ID', index=True, required=True, model_field='res_model', default=lambda self: self.env.ref('todo_list', False))
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Important'),
        ('2', 'Very Important'),
        ('3', 'Urgent'),
    ], default='0', index=True, store=True)
    recurring = fields.Boolean(string='Recurring', store=True)
    state = fields.Selection([
        ('today', 'Today'),
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('overdue', 'Expired'),
        ('cancel', 'Cancelled'),
    ], 'State', compute='_compute_state', store=True)
    interval = fields.Selection([
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly')
    ], string='Recurring Interval')
    new_date = fields.Date(string='Next Due Date', store=True)

    def action_cancel(self):
        return self.write({'state': 'cancel'})

    def action_date(self):
        return

    def get_date(self):
        """ Function for Get new due date on new Record"""
        date_deadline = self.new_date if self.new_date else self.date_deadline
        new_date = False
        if self.interval == 'Daily':
            new_date = (date_deadline + timedelta(days=1)).strftime(DEFAULT_SERVER_DATE_FORMAT)
        else:
            pass
        return new_date

#     function for show new due date
    @api.onchange('interval', 'date_deadline')
    def onchange_recurring(self):
        self.new_date = False
        if self.recurring:
            self.new_date = self.get_date()


class ActivityGeneral(models.Model):
    _name = 'activity.general'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')