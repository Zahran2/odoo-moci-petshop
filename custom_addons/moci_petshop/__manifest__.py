{
    'name': 'Moci Petshop Management',
    'version': '1.0',
    'category': 'Sales/Moci Petshop',
    'summary': 'Modul custom untuk manajemen Moci Petshop',
    'description': """
        Modul Odoo ERP untuk Moci Petshop:
        - Manajemen Data Hewan Peliharaan
        - Manajemen Layanan Grooming & Penitipan
    """,
    'author': 'Zahran Anugerah Rizqullah',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/petshop_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}