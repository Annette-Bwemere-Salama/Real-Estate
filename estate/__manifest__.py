{
    'name': 'Real Estate',
    'version': '1.0.0',
    'summary': 'The Real Estate Advertisement module',
    'description': 'Its A module for the advertisement',
    'author': 'Annette Salama',
    'depends': ['crm'],
    'installable': True,
    'application': True,
    'license': 'GPL-2',
    'data': [
        "security/estate_res_groups.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_tag.view.xml",
        "views/estate_property_type_views.xml",
        "views/estate_menus.xml",
        "views/estate_property_views.xml"
    ],
    'demo': [
        'demo/demo.xml'
    ],
}

