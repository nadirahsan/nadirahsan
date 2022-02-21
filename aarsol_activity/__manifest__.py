{
    'name': 'GLOBALXS Activities',
    'summary': 'GLOBALXS Activities',
    'description': """
        GLOBALXS Activities:
        
        This module adds an activity board with form, tree, kanban, calendar, pivot, graph and search views.
        
        A smartButton of activities is added in the mail thread from form view.
        From this smartButton is linked to the activity board, to the view tree,
        which shows the activities related to the opportunity.

        From the form view of the activity you can navigate to the origin of the activity.
        
        ***********
        This module implements the capability to keep activities that have been completed, for future reporting, by setting them with the boolean 'Done'.
        The activities that have been completed will not appear in the chatter.
        """,
    'version': '13.0.1.0.0',
    'category': 'Accounts',
    'website': 'http://www.globalxs.co',
    'author': 'GlobalXS Technology Solutions',
    'license': 'AGPL-3',
    'depends': [
        'calendar',
        'board',
        'mail',
    ],
    'data': [
        'views/templates.xml',
        'views/mail_activity_type_view.xml',
        'views/mail_activity_board_view.xml',
    ],
    'qweb': [
        'static/src/xml/inherit_chatter.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
