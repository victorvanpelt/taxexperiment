from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    form_model = 'player'
    form_fields = ['accept_conditions']

#class ResultsWaitPage(WaitPage):

    #def after_all_players_arrive(self):
        #pass

class Info_1(Page):
    form_model = 'player'
    form_fields = ['accept_continue']

class Info_2(Page):
    form_model = 'player'
    form_fields = ['inspectinfo', 'opinfo_timer', 'clinfo_timer', 'info_timer', 'subda_timer']

class Judgment(Page):
    form_model = 'player'
    form_fields = ['islider', 'iinvest', 'consultother', 'islider2', 'iinvest2', 'consultother2']

class Financial(Page):
    form_model = 'player'
    form_fields = [
        'FL1',
        'FL2',
        'FL3',
        'FL4',
        'FL5',
        'FL6',
        'FL7',
        'FL8',
        'FL9',
        'FL10'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Experience(Page):
    form_model = 'player'
    form_fields = [
        'FE1',
        'FE2',
        'FE3',
        'FE4',
        'FE5',
        'FE6'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class PEQ(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'nationality',
        'employment',
        'education',
        'workexperience',
        'english'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Turk(Page):
    form_model = 'player'
    form_fields = [
        'mturk',
        'mturk_feedback'
    ]

class Thank(Page):
    pass


page_sequence = [
    Intro,
    Info_1,
    Info_2,
    Judgment,
    Financial,
    Experience,
    PEQ,
    Turk,
    Thank
]
