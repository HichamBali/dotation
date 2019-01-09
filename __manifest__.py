# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'dodation',
    'version': '0.1',
    'author': 'Hicham bali',
    'category': 'premier module',
    'description': "Ceci est mon prmier module du tp n_3",
    'depends': ['sale_management','hr'],
    'installable': True,
    'application': True,
    'data': [

	              'views/decharge.xml',
	              'views/extendingemploye.xml',
	              'views/lignedecharge.xml',
	              'views/extendingarticle.xml',
	              'report/decharge_report.xml'
	        ],
    'website' :'www.modulen1.com',
    'license' : 'GPL-2',
}
