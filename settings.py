from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings = {
    'keywords': ['financial', 'tax', 'study', 'academic', 'research', 'accounting', 'investment'],
    'title': 'Academic study ($1.25 for about 8 min)',
    'description': 'Academic study that pays $1.25 for about 8 minutes.',
    'frame_height': 500,
    #'preview_template': 'global/MTurkPreview.html',
    'template': 'global/mturk_template.html',
    'minutes_allotted_per_assignment': 45,
    'expiration_hours': 7*24, # 7 days
    'qualification_requirements': [
        # No-retakers
        {
            'QualificationTypeId': "30LLG2NWCXJ09FSUO3LGVGEKYUS095",
            'Comparator': "DoesNotExist",
        },
        # Only US
        {
            'QualificationTypeId': "00000000000000000071",
            'Comparator': "EqualTo",
            'LocaleValues': [{'Country': "US"}]
        },
        # At least x HITs approved
        {
            'QualificationTypeId': "00000000000000000040",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [500]
        },
        # At least x% of HITs approved
        {
            'QualificationTypeId': "000000000000000000L0",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [95]
        },
        ]
}

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 1.25,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'publictax_normal',
        'display_name': "Main Experiment - Australian Setting - 11% ETR",
        'num_demo_participants': 25,
        'app_sequence': ['publictax_button'],
        'etr': 1,
        'cbc': 0,
        'disclaim': 0,
    },
    {
        'name': 'publictax_extreme',
        'display_name': "Supplemental Experiment 1 - Australian Setting - 1% ETR",
        'num_demo_participants': 25,
        'app_sequence': ['publictax_button'],
        'etr': 2,
        'cbc': 0,
        'disclaim': 0,
    },
    {
        'name': 'publictax_normal_cbc',
        'display_name': "Supplemental Experiment 2 - CbC Setting - 11% ETR",
        'num_demo_participants': 4,
        'app_sequence': ['publictax_button'],
        'etr': 1,
        'cbc': 1,
        'disclaim': 0,
    },
    {
        'name': 'publictax_no_btn',
        'display_name': "Supplemental Experiment 3 - Australian Setting - No Button",
        'num_demo_participants': 25,
        'app_sequence': ['publictax'],
        'etr': 1,
        'cbc': 0,
        'disclaim': 0,
    },
    {
        'name': 'publictax_disclaimer',
        'display_name': "Supplemental Experiment 4 - Australian Setting - Disclaimer",
        'num_demo_participants': 25,
        'app_sequence': ['publictax_button_disclaimer'],
        'etr': 1,
        'cbc': 0,
        'disclaim': 1,
    },
    {
        'name': 'publictax_aggressive',
        'display_name': "Supplemental Experiment 5 - Australian Setting - Aggressiveness",
        'num_demo_participants': 25,
        'app_sequence': ['publictax_aggressive'],
        'etr': 1,
        'cbc': 0,
        'disclaim': 0,
    },
]

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

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

SECRET_KEY = '6w-&=9x6umsmu%ohlg!66jk3-&8bku#wpnz_j$0^)zi*58e3+1'

GOOGLE_RECAPTCHA_SECRET_KEY = '6LfmYcgUAAAAADCpMDcV_KzyfxiFJ0ZjZRmhLoXM'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']