from odoo import models,fields

class lignedecharge(models.Model):
    _name = "ligne"
    decharge = fields.Many2one('decharge')
    quantite = fields.Integer()
    article = fields.Many2one('product.template')
