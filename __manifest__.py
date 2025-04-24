# -*- coding: utf-8 -*-
{
    'name': "LWW Expense",

    'summary': "Custom di Modul Expense",

    'description': """

    """,

    'author': "PT Lintang Utama Infotek",
    'website': "https://www.lui.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Expense',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}