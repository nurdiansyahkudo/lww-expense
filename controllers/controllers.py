# -*- coding: utf-8 -*-
# from odoo import http


# class LwwExpense(http.Controller):
#     @http.route('/lww_expense/lww_expense', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lww_expense/lww_expense/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lww_expense.listing', {
#             'root': '/lww_expense/lww_expense',
#             'objects': http.request.env['lww_expense.lww_expense'].search([]),
#         })

#     @http.route('/lww_expense/lww_expense/objects/<model("lww_expense.lww_expense"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lww_expense.object', {
#             'object': obj
#         })

