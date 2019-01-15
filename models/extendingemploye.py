from odoo import fields , models , api

class extendingemploye(models.Model):
    _inherit = "hr.employee"

    decharge_count = fields.Integer(compute='_decharge_count', string='# of decharges')
    decharge = fields.One2many('decharge', 'employe', 'dechargelemployer')

    @api.one
    @api.depends('decharge')
    def _decharge_count(self):
        decharges = self.env['decharge'].search([('employe', '=', self.ids)])
        self.decharge_count = len(decharges)
