# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class lww_expense(models.Model):
#     _name = 'lww_expense.lww_expense'
#     _description = 'lww_expense.lww_expense'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

