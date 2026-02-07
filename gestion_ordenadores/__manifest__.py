{
    'name': 'Modulo Gestion Ordenadores',
    'version': '1.0',
    'summary': 'Gestión de ordenadores, componentes y mantenimiento',
    'description': """
        Módulo para gestionar el inventario de ordenadores de la empresa.
        Permite registrar:
        - Componentes
        - Ordenadores y sus especificaciones
        - Asignación a usuarios
    """,
    'author': 'Antigravity',
    'category': 'Inventory/Computer',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/component_views.xml',
        'views/computer_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
