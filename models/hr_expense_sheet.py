from odoo import models, fields, api

class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    release_date = fields.Date(string='Release Date')

    def _do_approve(self):
        sheets_to_approve = self.filtered(lambda s: s.state in {'submit', 'draft'})
        sheets_to_approve._check_can_create_move()
        sheets_to_approve._do_create_moves()

        for sheet in sheets_to_approve:
            sheet.write({
                'approval_state': 'approve',
                'user_id': sheet.user_id.id or self.env.user.id,
                'approval_date': fields.Date.context_today(sheet),
            })
            # Update release_date on each expense line
            if sheet.release_date:
                sheet.expense_line_ids.write({
                    'release_date': sheet.release_date
                })

        self.activity_update()