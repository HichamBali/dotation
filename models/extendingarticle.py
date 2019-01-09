from odoo import fields , models

class extendingarticle(models.Model):
    _inherit = "product.template"
    isdotation = fields.Boolean("Is dotation", default=False)
