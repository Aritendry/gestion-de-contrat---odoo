from odoo import fields, models

class Contract(models.Model):
    _name = 'contract.contract'
    _description = 'Contract'

    name = fields.Char('Contract Name', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    amount = fields.Float('Amount', required=True)
    customer_id=fields.Many2one('res.partner', string='Customer')