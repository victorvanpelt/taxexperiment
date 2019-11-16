import random
from django import forms
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian Peters and Victor van Pelt'

doc = """
Public Tax Experiment Software
"""


class Constants(BaseConstants):
    name_in_url = 'publictax'
    players_per_group = None
    num_rounds = 1
    AgreeChoices=[
        [1, 'Disagree strongly'],
        [2, 'Disagree moderately'],
        [3, 'Disagree a little'],
        [4, 'Neither agree nor disagree'],
        [5, 'Agree a little'],
        [6, 'Agree moderately'],
        [7, 'Agree strongly'],
    ]
    DefinitelyChoices=[
        [1, 'Definitely not'],
        [2, 'Very unlikely'],
        [3, 'Unlikely'],
        [4, 'Neutral'],
        [5, 'Likely'],
        [6, 'Very likely'],
        [7, 'Definitely'],
    ]

class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        for player in self.get_players():
            player.treat = random.choice(['control', 'credit', 'credit_p', 'shift', 'shift_p'])

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treat = models.StringField()
    accept_conditions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)

    # Instruction checks
    Instr1 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)

    timer_id = models.StringField(blank=True)

# Financial Literacy
    FL1 = models.IntegerField(
        label = "Suppose you had $100 in a savings account and the interest rate was 2% per year. After 5 years, how much do you think you would have in the account if you left the money to grow?",
        choices = [
            [1, 'More than $102'],
            [2, 'Exactly $102'],
            [3,'Less than $102'],
            [4,"I don't know"]
        ],
        widget = widgets.RadioSelect
    )

    FL2 = models.IntegerField(
        label = "Suppose you had $100 in a savings account and the interest rate is 20% per year and you never withdraw money or interest payments. After 5 years, how much would you have on this account in total?",
        choices = [
            [1, 'More than $200'],
            [2, 'Exactly $200'],
            [3, 'Less than $200'],
            [4, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL3 = models.IntegerField(
        label = "Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per year. After 1 year, how much would you be able to buy with the money in this account?",
        choices = [
            [1, 'More than today'],
            [2, 'Exactly the same as today'],
            [3, 'Less than today'],
            [4, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL4 = models.IntegerField(
        label = "Assume a friend inherits $10,000 today and his sibling inherits $10,000 three years from now. Assume both your friend and his sibling do not spend the $10,000. Who is richer because of the inheritance?",
        choices = [
            [1, 'My friend'],
            [2, 'His sibling'],
            [3, 'They are equally rich'],
            [4, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL5 = models.IntegerField(
        label = "Suppose that in the year 2020, your income has doubled, and prices of all goods have doubled too. In 2020, how much will you be able to buy with your income?",
        choices = [
            [1, 'More than today'],
            [2, 'Exactly the same'],
            [3, 'Less than today'],
            [4, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL6 = models.IntegerField(
        label = "Which of the following financial assets typically grant you the highest return over a long period of time (e.g., 10-20 years)?",
        choices = [
            [1, 'Savings accounts'],
            [2, 'Individual shares and stocks'],
            [3, 'Debt securities and bonds'],
            [4, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL7 = models.IntegerField(
        label = "If the interest rate drops, what happens to bond prices?",
        choices = [
            [1, 'They rise'],
            [2, 'They fall'],
            [3, 'They stay the same'],
            [4, 'I do not know']
        ],
        widget=widgets.RadioSelect
    )

    FL8 = models.IntegerField(
        label = "Compared to similar firms in the same industry, a company uses more borrowed money to finance its operations. Which of the following statements is most likely to be true for the company?",
        choices = [
            [1, 'It is less likely to experience any difficulty with its creditors compared to other firms in the industry'],
            [2, 'It has less liquidity than other firms in the industry'],
            [3, 'It will be viewed as having relatively high creditworthiness'],
            [4, 'It has greater than average financial risk when compared to other firms in the industry'],
            [5, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL9 = models.IntegerField(
        label="Which of the following activities would most likely result in an increased risk of the firm being unable to repay borrowed funds?",
        choices = [
            [1, 'Increasing short-term assets while decreasing short-term liabilities'],
            [2, 'Increasing short-term assets while increasing short-term liabilities'],
            [3, 'Reducing short-term assets, increasing short-term liabilities, and reducing long-term liabilities'],
            [4, 'Replacing short-term liabilities with equity'],
            [5, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

    FL10 = models.IntegerField(
        label = "Which of the following statements is correct? If somebody buys a bond of firm B:",
        choices = [
            [1, "He owns a part of firm B"],
            [2, "He has lent money to firm B"],
            [3, "He is liable for firm B's debts"],
            [4, "None of the above"],
            [5, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

# PEQ_1 Process Variables

    rd = models.IntegerField(
        label="Alophonica’s innovativeness influenced my decision about it paying its fair share of taxes",
        choices=Constants.AgreeChoices
    )

    australia_check = models.BooleanField(
        label="The tax authorities of Olmeos disclosed information about Alophonica’s operations in Olmeos."
    )

    cbc_check = models.BooleanField(
        label="The tax authorities of Olmeos disclosed information about Alophonica’s operations in other countries than Olmeos.",
    )

    fair_rd = models.IntegerField(
        label="It is fair to lower taxes using investment tax credits.",
        choices=Constants.AgreeChoices
    )

    fair_ps = models.IntegerField(
        label="It is fair to lower taxes by shifting profits to countries with lower statutory tax rate such as Hingland.",
        choices=Constants.AgreeChoices
    )

    fair_more = models.IntegerField(
        label="It is fairer to lower taxes by shifting profit than by using investment tax credits.",
        choices=Constants.AgreeChoices
    )

    fair_ptd = models.IntegerField(
        label="The information disclosed by Olmeos' tax authorities influenced my decision about Alophonica paying its fair share of taxes.",
        choices=Constants.AgreeChoices
    )

    fair_report = models.IntegerField(
        label="The information in Alophonica's financial report influenced my decision about Alophonica paying its fair share of taxes.",
        choices=Constants.AgreeChoices
    )

    # PEQ_2

    gender = models.IntegerField(
        label="Please select your gender.",
        blank=False,
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
            [4, "I prefer not to say"]
        ]
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
            [7, 'I prefer not to say']
        ]
    )

    employment = models.IntegerField(
        label = "Please select what best describes your current employment status.",
        choices = [
            [1, "Working full-time"],
            [2, "Working part-time"],
            [3, "Unemployed and looking for work"],
            [4, "Unemployed and not looking for work"],
            [5, "Retired"],
            [6, "Student"],
            [7, "I prefer not to say"]
        ]
    )

    education = models.IntegerField(
        label = "What is the highest level of education that you have completed?",
        choices = [
            [1, 'Less than High school'],
            [2, 'High school'],
            [3, 'Vocational or trade school'],
            [4, '2-year College'],
            [5, '4-year College (BS, BA, or similar)'],
            [6, 'Postgraduate (MS, MA, PhD, MBA, MD, etc.)'],
            [7, 'I prefer not to say']
        ]
    )

    workexperience = models.IntegerField(
        label="Please indicate your work experience. All jobs count, including part-time and volunteer work.",
        blank=False,
        choices=[
            [1, 'I do not have work experience.'],
            [2, 'Less than 5 year work experience.'],
            [3, 'Between 5 and less than 10 years of work experience'],
            [4, 'Between 10 and less than 20 years work experience.'],
            [5, 'Between 20 and less than 30 years work experience.'],
            [6, 'Between 30 and less than 40 years work experience.'],
            [7, '40 years or more work experience.']
        ]
    )

    english = models.IntegerField(
        label="Please rate your English on a percentage scale between 0 and 100.",
        min=0,
        max=100,
        blank=False,
        initial=None
    )

    politics = models.IntegerField(
        label="Please indicate which political party best describes your political orientation.",
        choices=[
            [1, 'Democrats'],
            [2, 'Republicans'],
            [3, 'Other'],
            [4, 'Prefer not to say']
        ]
    )

    tax_advisor = models.IntegerField(
        label="How often do you consult a tax advisor, both privately or as part of your job?",
        choices=[
            [1, 'Never'],
            [2, 'Very rarely'],
            [3, 'Rarely'],
            [4, 'Sometimes'],
            [5, 'Occasionally'],
            [6, 'Frequently'],
            [7, 'Very frequently']
        ]
    )

    TA_1 = models.IntegerField(
        label="To what extent do you think claiming state benefits to which one is not entitled is justified?",
        choices=[
            [1, '1: Never Justified'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10: Always Justified']
        ]
    )

    TA_2 = models.IntegerField(
        label="To what extent do you think that cheating on taxes if one had the chance is justified?",
        choices=[
            [1, '1: Never Justified'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10: Always Justified']
        ]
    )

    TA_3 = models.IntegerField(
        label="To what extent do you think that avoiding taxes by using legal means if given the chance is justified?",
        choices=[
            [1, '1: Never Justified'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10: Always Justified']
        ]
    )

    Function = models.IntegerField(
        label="In which function of your organization do you currently work (please check one)?",
        choices=[
            [1, 'General Management'],
            [2, 'Operations'],
            [3, 'Finance/Accounting'],
            [4, 'Marketing/Sales'],
            [5, 'Human Resources'],
            [6, 'R&D'],
            [7, 'Other'],
            [8, 'None, I am unemployed']
        ]
    )

    Industry = models.IntegerField(
        label="In which industry does your firm primarily conduct business?",
        choices=[
            [1, 'Mining/Oil/Gas'],
            [2, 'Construction'],
            [3, 'Transportation'],
            [4, 'Manufacturing'],
            [5, 'Retail'],
            [6, 'Financial Services'],
            [7, 'Health Care'],
            [8, 'Other Services'],
            [9, 'Not-For-Profit'],
            [10, 'Government'],
            [11, 'Other'],
            [12, 'None, I am unemployed']
        ]
    )

# Experience Questions for PEQ_2
    fin_exp = models.IntegerField(
        label="I have experience with conducting trades and transactions with financial assets such as debt securities, bonds, shares, financial funds, and derivatives.",
        choices=Constants.AgreeChoices
    )
    fin_own = models.IntegerField(
        label="I have indirectly or directly owned financial assets such as debt securities, bonds, shares, mutual or pension funds, and derivatives.",
        choices=Constants.AgreeChoices
    )
    tax_exp = models.IntegerField(
        label="I have been involved in making tax management policies and setting out tax strategies for firms.",
        choices=Constants.AgreeChoices
    )
    tax_an = models.IntegerField(
        label="I have experience with analyzing and evaluating firms' tax management strategies and policies.",
        choices=Constants.AgreeChoices
    )

# Investor Judgments

    i_judge_1 = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
        )

    check_i_judge_1 = models.FloatField(blank=True, initial=None)

    i_judge_2 = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
    )

    check_i_judge_2 = models.FloatField(blank=True, initial=None)

    i_judge_3 = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
        )

    check_i_judge_3 = models.FloatField(blank=True, initial=None)

    i_market = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px', 'autocomplete':'off'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
    )
    check_i_market= models.FloatField(blank=True, initial=None)

# Fair Share

    alotax = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=False),
        min=-100,
        initial=None,
        max=100,
        )

    check_alotax = models.FloatField(blank=True, initial=None)

# End of HIT MTurk

    mturk = models.IntegerField(
        label = "How difficult was this HIT?",
        choices = [
            [1, 'Extremely easy'],
            [2, 'Moderately easy'],
            [3, 'Slightly easy'],
            [4, 'Neither easy nor difficult'],
            [5, 'Slightly difficult'],
            [6, 'Moderately difficult'],
            [7, 'Extremely difficult'],
            ],
        blank=True
    )

    mturk_feedback = models.StringField(
        label = "Do you have any feedback for us or anything you would like to say to us",
        blank=True
    )

    mturk_motivation = models.IntegerField(
        label = "How motivated were you during this HIT?",
        choices = [
            [1, 'Extremely unmotivated'],
            [2, 'Very unmotivated'],
            [3, 'Unmotivated'],
            [4, 'Neutral'],
            [5, 'Motivated'],
            [6, 'Very motivated'],
            [7, 'Extremely motivated']
        ]
    )