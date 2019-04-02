from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_model = 'player'
    form_fields = ['accept_conditions']

#class ResultsWaitPage(WaitPage):

    #def after_all_players_arrive(self):
        #pass

class Info(Page):
    pass

class Judgment(Page):
    form_model = 'player'
    form_fields = ['inspectinfo']

class Financial(Page):
    pass

class Thank(Page):
    pass


page_sequence = [
    Intro,
    Info,
    #ResultsWaitPage,
    Judgment,
    Financial,
    Thank
]
