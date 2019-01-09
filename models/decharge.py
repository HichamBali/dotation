from odoo import models,fields
from datetime import datetime

class decharge(models.Model):
    _name = "decharge"
    date = fields.Date()
    employe = fields.Many2one('hr.employee')
    lignedech = fields.One2many('ligne', 'decharge', 'ligne')
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('valide', 'Valide'),
    ], string='Status', default='brouillon')

