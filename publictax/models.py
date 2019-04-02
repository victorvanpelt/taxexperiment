import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian Peters'

doc = """
Public Tax Experiment Software
"""


class Constants(BaseConstants):
    name_in_url = 'publictax'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        for player in self.get_players():
            player.treat = random.choice(['gaap', 'country','full'])
            #print('set player.color to', player.color)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.StringField()
    accept_conditions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    inspectinfo = models.IntegerField(blank=True, initial=0)