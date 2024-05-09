# -*- coding: utf-8 -*-
# from odoo import http


# class TodoList(http.Controller):
#     @http.route('/todo_list/todo_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_list/todo_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_list.listing', {
#             'root': '/todo_list/todo_list',
#             'objects': http.request.env['todo_list.todo_list'].search([]),
#         })

#     @http.route('/todo_list/todo_list/objects/<model("todo_list.todo_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_list.object', {
#             'object': obj
#         })
