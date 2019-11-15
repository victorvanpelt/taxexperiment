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

class Info(Page):
    form_model = 'player'
    form_fields = ['Instr1', 'Instr2', 'Instr3']

    # def error_message(self, values):
    #     if values["Instr1a"] != 1:
    #         return 'Your first answer is incorrect. Check the instructions to understand what the task of this HIT is.'
    #     if values["Instr1b"] != 2:
    #         return 'Your second answer is incorrect. Check the instructions to understand the difference between statutory and effective tax rates.'

class E_judge(Page):
    form_model = 'player'
    form_fields = ['timer_id', 'alotax', 'check_alotax']

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_alotax"] == None:
                return 'Please the slider to make a decision.'

class I_judge(Page):
    form_model = 'player'
    form_fields = ['i_judge_1', 'i_judge_2', 'i_judge_3', 'check_i_judge_1', 'check_i_judge_2', 'check_i_judge_3', 'i_market', 'check_i_market',]

    def error_message(self, value):
        #if self.group.r == None:
            if value["check_i_judge_1"] == None:
                return 'Please drag all four sliders to make your decisions.'
            if value["check_i_judge_2"] == None:
                return 'Please drag all four sliders to make your decisions.'
            if value["check_i_judge_3"] == None:
                return 'Please drag all four sliders to make your decisions.'
            if value["check_i_market"] == None:
                return 'Please drag all four sliders to make your decisions.'

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

class Peq_1(Page):
    form_model = 'player'
    form_fields = [
        'rd',
        'fair_rd',
        'fair_ps',
        'fair_more',
        'australia_check',
        'cbc_check'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Peq_2(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'politics',
        'nationality',
        'employment',
        'education',
        'workexperience',
        'english',
        'tax_advisor',
        'fin_exp',
        'fin_own',
        'tax_exp',
        'tax_an',
        'TA_1',
        'TA_2',
        'TA_3',
        'Function',
        'Industry'
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

# class Mba(Page):
#     form_model = 'player'
#     form_fields = [
#         'mturk_feedback',
#     ]

page_sequence = [
    Intro,
    Info,
    E_judge,
    I_judge,
    Peq_1,
    Financial,
    Peq_2,
    Turk
]
