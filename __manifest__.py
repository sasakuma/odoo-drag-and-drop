"""
Copyright (C) Andreas Wyrobek - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Andreas Wyrobek <andreas.wyrobek95@gmail.com>, December 2017
"""

# -*- coding: utf-8 -*-
{
    'name': "Drag & Drop",

    'summary': """
        Drag and Drop Attachments without limits. Upload Screenshots easily.
    """,

    'author': "Andreas Wyrobek",
    'website': "http://www.cytex.cc",

    'category': 'Administration',
    'version': '0.1',

    'price': 29.99,
    'currency': 'EUR',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'document', 'web'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}