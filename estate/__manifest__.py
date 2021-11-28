
{
    'name': 'Real Estate',
    'description': 'Test Modul',
    'category': 'Sales',
    'application':True,
    'depends': ['base','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
    ],
}