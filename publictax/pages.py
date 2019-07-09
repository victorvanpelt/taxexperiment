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
    form_fields = ['Instr1a', 'Instr1b']

    def error_message(self, values):
        if values["Instr1a"] != 1:
            return 'Your first answer is incorrect. Check the instructions to understand what the task of this HIT is.'
        if values["Instr1b"] != 2:
            return 'Your second answer is incorrect. Check the instructions to understand the difference between statutory and effective tax rates.'

class Info_2(Page):
    form_model = 'player'
    form_fields = ['Instr2a', 'Instr2b']

    def error_message(self, values):
        if values["Instr2a"] != 2:
            return 'Your first answer is incorrect. Check the instructions to understand where both countries are headquartered and where they operate.'
        if values["Instr2b"] != 1:
            return 'Your second answer is incorrect. Check the instructions to understand how statutory and effective tax rates can differ.'

class Info_3(Page):
    form_model = 'player'
    form_fields = ['timer_id', 'alotax', 'beltax', 'check_alotax', 'check_beltax']

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_alotax"] == None:
                return 'Please drag both sliders to make your decisions'
            if value["check_beltax"] == None:
                return 'Please drag both sliders to make your decisions'

class Judgment(Page):
    form_model = 'player'
    form_fields = ['islider', 'iinvest', 'consultother', 'islider2', 'iinvest2', 'consultother2', 'check_islider', 'check_islider2', 'imarketslider', 'check_imarketslider']

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_islider"] == None:
                return 'Please drag all sliders to make your decisions'
            if value["check_islider2"] == None:
                return 'Please drag all sliders to make your decisions'
            if value["check_imarketslider"] == None:
                return 'Please drag x sliders to make your decisions'

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

# class Experience(Page):
#     form_model = 'player'
#     form_fields = [
#         'FE1',
#         'FE2',
#         'FE3',
#         'FE4',
#         'FE5',
#         'FE6'
#     ]
#
#     def get_form_fields(self):
#         fields = self.form_fields
#         random.shuffle(fields)
#         return fields

class PEQ(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'nationality',
        'employment',
        'education',
        'workexperience',
        'english',
        'politics',
        'tax_advisor'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Turk(Page):
    form_model = 'player'
    form_fields = [
        'mturk',
        'mturk_feedback',
        'mturk_motivation'
    ]

page_sequence = [
    Intro,
    Info_1,
    Info_2,
    Info_3,
    Judgment,
    Financial,
    # Experience,
    PEQ,
    Turk
]
