from odoo import models, fields

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    release_date = fields.Date(string='Release Date', related='sheet_id.release_date', store=True)