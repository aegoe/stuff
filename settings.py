from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'questionnaire',
        'display_name': "Questionnaire True",
        'num_demo_participants': 2,
        'app_sequence': ['questionnaire'],
        'treatment': True
    },
    {
        'name': 'questionnaireFalse',
        'display_name': "Questionnaire False",
        'num_demo_participants': 2,
        'app_sequence': ['questionnaire'],
        'treatment': False
    },
    {
        'name': 'first_app',
        'display_name': "My First App",
        'num_demo_participants': 1,
        'app_sequence': ['first_app'],
    },
    {
        'name': 'trust_game',
        'display_name': "Trust Game",
        'num_demo_participants': 2,
        'app_sequence': ['trust_game'],
    },
    {
        'name': 'public_goods_game_baseline',
        'display_name': "Public Good Game - Baseline",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_game'],
        'use_browser_bots': False,
        'hetero_endowment': False,
    },
    {
        'name': 'public_goods_game_het',
        'display_name': "Public Good Game - Het",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_game'],
        'use_browser_bots': False,
        'hetero_endowment': True,
    },
]



# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'vw_+s(_(r-00_9$ck@*@_0_m7wfabv5hbdrk$*65#nd1*kxaa='

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
