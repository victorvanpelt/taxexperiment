import itertools
import random

#from django import forms
from otree.api import *


author = 'Christian Peters and Victor van Pelt'
doc = """
Public Tax Experiment in oTree
"""


class Constants(BaseConstants):
    name_in_url = 'publictax_equnum'
    players_per_group = None
    num_rounds = 1
    completion_code = 'TAX_whu_112024'
    AgreeChoices = [
        [1, 'Strongly disagree'],
        [2, 'Disagree'],
        [3, 'Somewhat disagree'],
        [4, 'Neither agree nor disagree'],
        [5, 'Somewhat agree'],
        [6, 'Agree'],
        [7, 'Strongly agree'],
    ]
    DefinitelyChoices = [
        [1, 'Definitely not'],
        [2, 'Very unlikely'],
        [3, 'Unlikely'],
        [4, 'Neutral'],
        [5, 'Likely'],
        [6, 'Very likely'],
        [7, 'Definitely'],
    ]
    FrequencyChoices = [
        [1, 'Never'],
        [2, 'Rarely'],
        [3, 'Sometimes'],
        [4, 'Often'],
        [5, 'Always'],
    ]
    ImportantChoices = [
        [1, 'Not at all important'],
        [2, 'Low importance'],
        [3, 'Slightly important'],
        [4, 'Moderately important'],
        [5, 'Important'],
        [6, 'Very important'],
        [7, 'Extremely important'],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completion_code = models.StringField()
    etr = models.IntegerField()
    treat = models.StringField()
    accept_conditions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    accept_important = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    # Instruction checks
    Instr1 = models.IntegerField(
        blank=False,
        choices=[[1, 'True'], [2, 'False']],
        widget=widgets.RadioSelect,
        label='Telecom Co. is headquartered in Country A.',
    )
    Instr2 = models.IntegerField(
        blank=False,
        choices=[[1, 'True'], [2, 'False']],
        widget=widgets.RadioSelect,
        label='A tax rate of 24% means that companies pay 24% of profit before taxes.',
    )
    Instr3 = models.IntegerField(
        blank=False,
        choices=[[1, 'True'], [2, 'False']],
        widget=widgets.RadioSelect,
        label='The more Telecom Co. invests in business operations in Country B, the fewer taxes it effectively pays in Country B.',
    )
    Instr4 = models.IntegerField(
        blank=False,
        choices=[[1, 'True'], [2, 'False']],
        widget=widgets.RadioSelect,
        label='The tax rate of the other country in the example is higher than Country A.',
    )
    Instr5 = models.IntegerField(
        blank=False,
        choices=[[1, 'True'], [2, 'False']],
        widget=widgets.RadioSelect,
        label='Telecom Co. can pay less tax in Country A by shifting profits from Country A to the other country, which creates a tax difference due to foreign profits.',
    )
    # Instr6 = models.IntegerField(
    #     blank=False,
    #     choices=[[1, 'True'], [2, 'False']],
    #     widget=widgets.RadioSelect,
    #     label='The tax rate in Country A and Country B are the same.',
    # )



    timer_id = models.StringField(blank=True)
    # Financial Literacy
    FL1 = models.IntegerField(
        label="Suppose you had $100 in a savings account and the interest rate was 2% per year. After 5 years, how much do you think you would have in the account if you left the money to grow?",
        choices=[
            [1, 'More than $102'],
            [2, 'Exactly $102'],
            [3, 'Less than $102'],
            [4, "I don't know"],
        ],
        widget=widgets.RadioSelect,
    )
    FL2 = models.IntegerField(
        label="Suppose you had $100 in a savings account and the interest rate is 20% per year and you never withdraw money or interest payments. After 5 years, how much would you have on this account in total?",
        choices=[
            [1, 'More than $200'],
            [2, 'Exactly $200'],
            [3, 'Less than $200'],
            [4, "I don't know"],
        ],
        widget=widgets.RadioSelect,
    )
    FL3 = models.IntegerField(
        label="Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per year. After 1 year, how much would you be able to buy with the money in this account?",
        choices=[
            [1, 'More than today'],
            [2, 'Exactly the same as today'],
            [3, 'Less than today'],
            [4, "I don't know"],
        ],
        widget=widgets.RadioSelect,
    )
    FL4 = models.IntegerField(
        label="Assume a friend inherits $10,000 today and his sibling inherits $10,000 three years from now. Assume both your friend and his sibling do not spend the $10,000. Who is richer because of the inheritance?",
        choices=[
            [1, 'My friend'],
            [2, 'His sibling'],
            [3, 'They are equally rich'],
            [4, "I don't know"],
        ],
        widget=widgets.RadioSelect,
    )
    FL5 = models.IntegerField(
        label="Suppose that in the year 2020, your income has doubled, and prices of all goods have doubled too. In 2020, how much will you be able to buy with your income?",
        choices=[
            [1, 'More than today'],
            [2, 'Exactly the same'],
            [3, 'Less than today'],
            [4, "I don't know"],
        ],
        widget=widgets.RadioSelect,
    )
    # PEQ 1
    australia_check = models.IntegerField(
        label="In addition to Telecom Co.'s financial report, which you could reveal by pressing the button, what else was disclosed?",
        choices=[
            [1, "Nothing"],
            [2, "A table containing Revenues, Profit Before Tax, and Corporate Taxes"],
            [3, "I don't know"],
        ],
    )
    taxmanagement_check = models.IntegerField(
        label="Which tax management strategy did Telecom Co. follow to pay less than the tax rate?",
        choices=[
            [1, "Shifting profits to countries with a lower tax rate"],
            [2, "Using investment tax credits"],
            [3, "Both shifting profits and using investment tax credits"],
            [4, "Telecom Co. did not use a tax management strategy’"],
            [5, "I don't know"],
        ],
    )
    assessments_confident = models.IntegerField(
        label="I am confident about the assessments about Telecom Co. I made on the previous screens.",
        choices=Constants.AgreeChoices,
    )
    assessments_random = models.IntegerField(
        label="I made my assessments on the previous screens in a more or less random way.",
        choices=Constants.AgreeChoices,
    )
    assessments_no_use = models.IntegerField(
        label="I did not really know how I should use the financial information to make my assessments.",
        choices=Constants.AgreeChoices,
    )
    # PEQ_2
    fair_rd = models.IntegerField(
        label="•	In general, I consider it fair if companies lower taxes by using Investment tax credits in another country with the same tax rate.",
        choices=Constants.AgreeChoices,
    )
    fair_ps = models.IntegerField(
        label="In general, I consider it fair if companies lower taxes by shifting profits to countries with a lower tax rate.",
        choices=Constants.AgreeChoices,
    )
    fair_more = models.IntegerField(
        label="In general, I consider it fairer if companies lower taxes by shifting profits to countries with a lower tax rate than when companies use investment tax credits in another country with the same tax rate.",
        choices=Constants.AgreeChoices,
    )
    tax_advisor = models.IntegerField(
        label="How often do you consult a tax advisor, both privately and as part of your job?",
        choices=[
            [1, 'Never'],
            [2, 'Very rarely'],
            [3, 'Rarely'],
            [4, 'Sometimes'],
            [5, 'Occasionally'],
            [6, 'Frequently'],
            [7, 'Very frequently'],
        ],
    )
    TA_1 = models.IntegerField(
        label="Cheating on taxes if one had the chance is justified.",
        choices=[
            [1, 'Very untrue of what I believe'],
            [2, 'Untrue of what I believe'],
            [3, 'Somewhat untrue of what I believe'],
            [4, 'Neutral'],
            [5, 'Somewhat true of what I believe'],
            [6, 'True of what I believe'],
            [7, 'Very true of what I believe'],
        ],
    )
    TA_2 = models.IntegerField(
        label="Claiming state benefits to which one is not entitled is justified.",
        choices=[
            [1, 'Very untrue of what I believe'],
            [2, 'Untrue of what I believe'],
            [3, 'Somewhat untrue of what I believe'],
            [4, 'Neutral'],
            [5, 'Somewhat true of what I believe'],
            [6, 'True of what I believe'],
            [7, 'Very true of what I believe'],
        ],
    )
    TA_3 = models.IntegerField(
        label="Reducing taxes by using legal means is justified.",
        choices=[
            [1, 'Very untrue of what I believe'],
            [2, 'Untrue of what I believe'],
            [3, 'Somewhat untrue of what I believe'],
            [4, 'Neutral'],
            [5, 'Somewhat true of what I believe'],
            [6, 'True of what I believe'],
            [7, 'Very true of what I believe'],
        ],
    )
    taxmanagement_important = models.IntegerField(
        label="How important do you consider a company's tax management strategy when developing your overall opinion about a company?",
        choices=Constants.ImportantChoices,
    )
    # Experience Questions for PEQ_2
    fin_exp = models.IntegerField(
        label="How familiar are you with conducting trades and transactions with financial assets such as debt securities, bonds, shares, financial funds, and derivatives.",
        choices=[
            [1, 'Not at all familiar'],
            [2, 'Slightly familiar'],
            [3, 'Somewhat familiar'],
            [4, 'Moderately familiar'],
            [5, 'Extremely familiar'],
        ],
    )
    fin_own = models.IntegerField(
        label="I own or have indirectly or directly owned financial assets such as debt securities, bonds, shares, mutual or pension funds, and derivatives.",
        choices=[
            [1, 'Never'],
            [2, 'Very rarely'],
            [3, 'Rarely'],
            [4, 'Sometimes'],
            [5, 'Occasionally'],
            [6, 'Frequently'],
            [7, 'Very frequently'],
        ],
    )
    tax_exp = models.IntegerField(
        label="I have been involved in developing tax management policies and setting out tax strategies for companies.",
        choices=[
            [1, 'Never'],
            [2, 'Very rarely'],
            [3, 'Rarely'],
            [4, 'Sometimes'],
            [5, 'Occasionally'],
            [6, 'Frequently'],
            [7, 'Very frequently'],
        ],
    )
    tax_fam = models.IntegerField(
        label="How familiar are you with analyzing and evaluating companies' tax management strategies and policies?",
        choices=[
            [1, 'Not at all familiar'],
            [2, 'Slightly familiar'],
            [3, 'Somewhat familiar'],
            [4, 'Moderately familiar'],
            [5, 'Extremely familiar'],
        ],
    )
    tax_freq = models.IntegerField(
        label="How often do you look at a company's tax management strategy and policy when developing your opinion about a company?",
        choices=[
            [1, 'Never'],
            [2, 'Very rarely'],
            [3, 'Rarely'],
            [4, 'Sometimes'],
            [5, 'Occasionally'],
            [6, 'Frequently'],
            [7, 'Very frequently'],
        ],
    )
    # PEQ_3
    corona = models.IntegerField(
        label="I am worried about the Corona virus (COVID2019).", choices=Constants.AgreeChoices
    )
    gender = models.IntegerField(
        label="Please select which gender you identify most with.",
        blank=False,
        choices=[[1, 'Male'], [2, 'Female'], [3, 'Other'], [4, "I prefer not to say"]],
    )
    age = models.IntegerField(label="Please enter your age.", min=18, max=90, blank=False)
    nationality = models.IntegerField(
        label="Please select your region of residence.",
        blank=False,
        choices=[
            [1, 'North-America'],
            [2, 'Central and South-America'],
            [3, 'Asia'],
            [4, 'Europe'],
            [5, 'Australia and Oceania'],
            [6, 'Africa'],
            [7, 'I prefer not to say'],
        ],
    )
    employment = models.IntegerField(
        label="Please select what best describes your current employment status.",
        choices=[
            [1, "Working full-time"],
            [2, "Working part-time"],
            [3, "Unemployed and looking for work"],
            [4, "Unemployed and not looking for work"],
            [5, "Retired"],
            [6, "Student"],
            [7, "I prefer not to say"],
        ],
    )
    education = models.IntegerField(
        label="What is the highest level of education that you have completed?",
        choices=[
            [1, 'Less than High school'],
            [2, 'High school'],
            [3, 'Vocational or trade school'],
            [4, '2-year College'],
            [5, '4-year College (BS, BA, or similar)'],
            [6, 'Postgraduate (MS, MA, PhD, MBA, MD, etc.)'],
            [7, 'I prefer not to say'],
        ],
    )
    workexperience = models.IntegerField(
        label="Please indicate your work experience. All jobs count, including part-time and volunteer work.",
        blank=False,
        choices=[
            [1, 'I do not have work experience.'],
            [2, 'Less than 5 years work experience.'],
            [3, '5 to 10 years of work experience'],
            [4, '10 to 20 years work experience.'],
            [5, '20 to 30 years work experience.'],
            [6, '30 to 40 years work experience.'],
            [7, '40 years or more work experience.'],
        ],
    )
    english = models.IntegerField(
        label="Please rate your English on a percentage scale between 0 and 100.",
        min=0,
        max=100,
        blank=False,
        initial=None,
    )
    politics = models.IntegerField(
        label="Please indicate which political party best describes your political orientation.",
        choices=[[1, 'Democrats'], [2, 'Republicans'], [3, 'Other'], [4, 'Prefer not to say']],
    )
    # Attention checks for PEQ_3
    attention_1 = models.IntegerField(
        label="What rhymes with tree?", choices=[[1, 'box'], [2, 'crow'], [3, 'flee'], [4, 'car']]
    )
    # Interpersonal influence PEQ2
    norm_1 = models.IntegerField(
        label="When buying products, I generally purchase those brands that I think others will approve of.",
        choices=Constants.AgreeChoices,
    )
    norm_2 = models.IntegerField(
        label="If other people can see me using a product, I often purchase the brand they expect me to buy.",
        choices=Constants.AgreeChoices,
    )
    norm_3 = models.IntegerField(
        label="I achieve a sense of belonging by purchasing the same products and brands that others purchase.",
        choices=Constants.AgreeChoices,
    )
    # Investor Judgments
    i_judge_1 = models.FloatField(initial=None, blank=False, max=100, min=-100)
    # models.FloatField(
    # widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
    # min=-100,
    # initial=0,
    # max=100,
    # )
    check_i_judge_1 = models.FloatField(blank=True, initial=None)
    i_judge_2 = models.FloatField(initial=None, blank=False, max=100, min=-100)
    #     models.FloatField(
    #     widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
    #     min=-100,
    #     initial=0,
    #     max=100,
    # )
    check_i_judge_2 = models.FloatField(blank=True, initial=None)
    i_judge_3 = models.FloatField(initial=None, blank=False, max=100, min=-100)
    # models.FloatField(
    # widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
    # min=-100,
    # initial=0,
    # max=100,
    # )
    check_i_judge_3 = models.FloatField(blank=True, initial=None)
    i_market = models.FloatField(initial=None, blank=False, max=100, min=-100)
    #     models.FloatField(
    #     widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
    #     min=-100,
    #     initial=0,
    #     max=100,
    # )
    check_i_market = models.FloatField(blank=True, initial=None)
    # Fair Share
    alotax = models.FloatField(initial=None, blank=False, max=100, min=0)
    check_alotax = models.FloatField(blank=True, initial=None)
    # End of HIT MTurk
    mturk = models.IntegerField(
        label="How difficult was this study?",
        choices=[
            [1, 'Extremely easy'],
            [2, 'Moderately easy'],
            [3, 'Slightly easy'],
            [4, 'Neither easy nor difficult'],
            [5, 'Slightly difficult'],
            [6, 'Moderately difficult'],
            [7, 'Extremely difficult'],
        ],
        blank=True,
    )
    mturk_feedback = models.TextField(
        label="Do you have any feedback for us or anything you would like to say to us?", blank=True
    )
    mturk_motivation = models.IntegerField(
        label="How motivated were you during this study?",
        choices=[
            [1, 'Extremely unmotivated'],
            [2, 'Very unmotivated'],
            [3, 'Unmotivated'],
            [4, 'Neutral'],
            [5, 'Motivated'],
            [6, 'Very motivated'],
            [7, 'Extremely motivated'],
        ],
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    # assign etr and cbc
    for player in subsession.get_players():
        # 1 equals high, 2 equals low
        etr = player.session.config['etr']
        player.etr = etr
        # 0 is off and 1 is on
        cbc = player.session.config['cbc']
    if etr == 1:
        # randomize to treatments without control
        if cbc == 0:
            treats = itertools.cycle(['credit', 'credit_p', 'shift', 'shift_p'])
            for player in subsession.get_players():
                player.treat = next(treats)
        else:
            treats = itertools.cycle(['credit_cbc', 'shift_cbc'])
            for player in subsession.get_players():
                player.treat = next(treats)
    else:
        treats = itertools.cycle(['credit', 'credit_p', 'shift', 'shift_p'])
        for player in subsession.get_players():
            player.treat = next(treats)
    # assign fixed completion code to player
    for player in subsession.get_players():
        player.completion_code = Constants.completion_code


# PAGES
class Intro(Page):
    pass


class Info_1(Page):
    form_model = 'player'
    form_fields = ['Instr1', 'Instr2']


class Info_2(Page):
    form_model = 'player'
    form_fields = ['Instr3']


class Info_3(Page):
    form_model = 'player'
    form_fields = ['Instr4', 'Instr5']


class Important(Page):
    form_model = 'player'
    form_fields = ['accept_important']


class E_judge(Page):
    form_model = 'player'
    form_fields = ['timer_id', 'alotax', 'check_alotax']

    @staticmethod
    def error_message(player: Player, value):
        # if self.group.r == None:
        if value["check_alotax"] == None:
            return 'Please drag the slider to make a decision.'


class I_judge(Page):
    form_model = 'player'
    form_fields = [
        'i_judge_1',
        'i_judge_2',
        'i_judge_3',
        'check_i_judge_1',
        'check_i_judge_2',
        'check_i_judge_3',
    ]

    @staticmethod
    def error_message(player: Player, value):
        # if self.group.r == None:
        if value["check_i_judge_1"] == None:
            return 'Please drag all sliders to make your decisions.'
        if value["check_i_judge_2"] == None:
            return 'Please drag all sliders to make your decisions.'
        if value["check_i_judge_3"] == None:
            return 'Please drag all sliders to make your decisions.'


class Peq1(Page):
    form_model = 'player'
    form_fields = [
        'taxmanagement_check',
        'australia_check',
        'assessments_confident',
        'assessments_random',
        'assessments_no_use',
    ]

    @staticmethod
    def get_form_fields(player: Player):
        fields = [
            'taxmanagement_check',
            'australia_check',
            'assessments_confident',
            'assessments_random',
            'assessments_no_use',
        ]
        random.shuffle(fields)
        return fields


class Peq2(Page):
    form_model = 'player'
    form_fields = [
        'fair_rd',
        'fair_ps',
        'fair_more',
        'tax_advisor',
        'fin_exp',
        'fin_own',
        'tax_exp',
        'tax_fam',
        'tax_freq',
        'TA_1',
        'TA_2',
        'TA_3',
        'taxmanagement_important',
    ]

    @staticmethod
    def get_form_fields(player: Player):
        fields = [
            'fair_rd',
            'fair_ps',
            'fair_more',
            'tax_advisor',
            'fin_exp',
            'fin_own',
            'tax_exp',
            'tax_fam',
            'tax_freq',
            'TA_1',
            'TA_2',
            'TA_3',
            'taxmanagement_important',
        ]
        random.shuffle(fields)
        return fields


class Financial(Page):
    form_model = 'player'
    form_fields = ['FL1', 'FL2', 'FL3', 'FL4', 'FL5']

    @staticmethod
    def get_form_fields(player: Player):
        fields = ['FL1', 'FL2', 'FL3', 'FL4', 'FL5']
        random.shuffle(fields)
        return fields


class Peq3(Page):
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
        'attention_1',
        'norm_1',
        'norm_2',
        'norm_3',
        'corona',
    ]

    @staticmethod
    def get_form_fields(player: Player):
        fields = [
            'gender',
            'age',
            'politics',
            'nationality',
            'employment',
            'education',
            'workexperience',
            'english',
            'attention_1',
            'norm_1',
            'norm_2',
            'norm_3',
            'corona',
        ]
        random.shuffle(fields)
        return fields


class M(Page):
    form_model = 'player'
    form_fields = ['mturk', 'mturk_feedback', 'mturk_motivation']


class Thank(Page):
    form_model = 'player'
    form_fields = ['completion_code']


page_sequence = [
    Intro,
    Info_1,
    Info_2,
    Info_3,
    Important,
    E_judge,
    I_judge,
    Peq1,
    Peq2,
    Financial,
    Peq3,
    M,
    Thank,
]
