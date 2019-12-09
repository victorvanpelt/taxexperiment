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
        [1, 'Strongly disagree'],
        [2, 'Disagree'],
        [3, 'Somewhat disagree'],
        [4, 'Neither agree nor disagree'],
        [5, 'Somewhat agree'],
        [6, 'Agree'],
        [7, 'Strongly agree'],
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
    FrequencyChoices=[
        [1, 'Never'],
        [2, 'Rarely'],
        [3, 'Sometimes'],
        [4, 'Often'],
        [5, 'Always'],
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        for player in self.get_players():
            player.treat = random.choice(['control', 'credit', 'credit_p', 'credit_cbc', 'shift', 'shift_p', 'shift_cbc'])

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treat = models.StringField()
    accept_conditions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)

    # Instruction checks
    Instr1 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr4 = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)

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
        label = "Which of the following financial assets typically grants you the highest return over a long period of time (e.g., 10-20 years)?",
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

# PEQ_1
    australia_check = models.IntegerField(
        label = "In addition to Alophonica's financial report which you could reveal by pressing the button, what else was disclosed?",
        choices = [
            [1, "The statutory tax rate in Olmeos is 24%"],
            [2, "The statutory tax rate in Olmeos is 24% and a table containing Alophonica's Revenues, Profit Before Tax, and Corporate Taxes Paid in Olmeos"],
            [3, "I don't know"]
        ]
    )

    taxmanagement_check = models.IntegerField(
        label = "Which tax management strategy did Alophonica follow to pay less than the statutory tax rate?",
        choices = [
            [1, "Shifting profits to countries with a lower statutory tax rate"],
            [2, "Using investment tax credits"],
            [3, "Both shifting profits and using investment tax credits"],
            [4, "Alophonica did not use a tax management strategy’"],
            [5, "I don't know"]
        ]
    )

    fair_rd = models.IntegerField(
        label="In general, I consider it fair if companies lower taxes by using investment tax credits.",
        choices=Constants.AgreeChoices
    )

    fair_ps = models.IntegerField(
        label="In general, I consider it fair if companies lower taxes by shifting profits to countries with a lower statutory tax rate.",
        choices=Constants.AgreeChoices
    )

    fair_more = models.IntegerField(
        label="In general, I consider it fairer if companies lower taxes by shifting profits to countries with a lower statutory tax rate than when companies use investment tax credits.",
        choices=Constants.AgreeChoices
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
            [7, 'Very frequently']
        ]
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
            [7, 'Very true of what I believe']
        ]
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
            [7, 'Very true of what I believe']
        ]
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
            [7, 'Very true of what I believe']
        ]
    )

    # Experience Questions for PEQ_2
    fin_exp = models.IntegerField(
        label="How familiar are you with conducting trades and transactions with financial assets such as debt securities, bonds, shares, financial funds, and derivatives.",
        choices=[
            [1, 'Not at all familiar'],
            [2, 'Slightly familiar'],
            [3, 'Somewhat familiar'],
            [4, 'Moderately familiar'],
            [5, 'Extremely familiar']
        ]
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
            [7, 'Very frequently']
        ]
    )
    tax_exp = models.IntegerField(
        label="I have been involved in developing tax management policies and setting out tax strategies for firms.",
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
    tax_fam = models.IntegerField(
        label="How familiar are you with analyzing and evaluating firms' tax management strategies and policies?",
        choices=[
            [1, 'Not at all familiar'],
            [2, 'Slightly familiar'],
            [3, 'Somewhat familiar'],
            [4, 'Moderately familiar'],
            [5, 'Extremely familiar']
        ]
    )
    tax_freq = models.IntegerField(
        label="How often do you look at a firm's tax management strategy and policy when developing your opinion about a firm?",
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

    # PEQ_2

    gender = models.IntegerField(
        label="Please select which gender you identify most with.",
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


# Attention checks for PEQ_2
    attention_1 = models.IntegerField(
        label="What rhymes on tree?",
        choices=[
            [1, 'box'],
            [2, 'crow'],
            [3, 'flee'],
            [4, 'car']
        ]
    )

# Interpersonal influence PEQ2
    norm_1 = models.IntegerField(
        label="When buying products, I generally purchase those brands that I think others will approve of.",
        choices=Constants.AgreeChoices
    )

    norm_2 = models.IntegerField(
        label="If other people can see me using a product, I often purchase the brand they expect me to buy.",
        choices=Constants.AgreeChoices
    )

    norm_3 = models.IntegerField(
        label="I achieve a sense of belonging by purchasing the same products and brands that others purchase.",
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
        min=0,
        initial=None,
        max=100,
        )

    check_alotax = models.FloatField(blank=True, initial=None)

# End of HIT MTurk

    mturk = models.IntegerField(
        label = "How difficult was this study?",
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

    mturk_feedback = models.TextField(
        label = "Do you have any feedback for us or anything you would like to say to us?",
        blank=True
    )

    mturk_motivation = models.IntegerField(
        label = "How motivated were you during this study?",
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