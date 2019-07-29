import random
from django import forms
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
            player.treat = random.choice(['control', 'australia', 'punish', 'full'])
            player.judgorder = random.choice(['A', 'B'])
            player.higher = random.choice(['A', 'B'])
            #print('set player.color to', player.color)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.StringField()
    higher = models.StringField()
    judgorder = models.StringField()
    accept_conditions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    # accept_continue1 = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    # accept_continue2 = models.BooleanField(blank=False, widget=widgets.CheckboxInput)

    # Instruction1 checks
    Instr1a = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr1b = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)

    # Instruction2 checks
    Instr2a = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2b = models.IntegerField(blank=False, choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)

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
        label = "Please indicate which of the following you think best captures the operating performance of a firm.",
        choices = [
            [1, "The return of a company's stock"],
            [2, "The value of sales performance of a firm"],
            [3, "The difference between total sales and cost of sales"],
            [4, "The net income generated relative to the value of a firm's total assets"],
            [5, "I don't know"]
        ],
        widget=widgets.RadioSelect
    )

# Financial Experience

    FE1 = models.StringField(
        blank=True,
        label="Please indicate whether you have directly or indirectly (e.g., through a pension or formal retirement) conducted trades and transactions in the following financial assets in the past:",
        widget=forms.CheckboxSelectMultiple(
            choices=[
                ['1', 'Debt securities and bonds'],
                ['2', 'Individual shares and stocks'],
                ['3', 'Mutual Funds'],
                ['4', 'Pension Funds'],
                ['5', 'Derivatives and options'],
                ['6', 'Other financial assets'],
            ],
        )
    )

    FE2 = models.StringField(
        blank=True,
        label="Please indicate whether you plan to own directly or indirectly (e.g., through a pension or formal retirement) one or more of the following financial assets in the future:",
        widget=forms.CheckboxSelectMultiple(
            choices=[
                ['1', 'Debt securities and bonds'],
                ['2', 'Individual shares and stocks'],
                ['3', 'Mutual Funds'],
                ['4', 'Pension Funds'],
                ['5', 'Derivatives and options'],
                ['6', 'Other financial assets'],
            ],
        )
    )

    FE3 = models.StringField(
        blank=True,
        label="Please indicate whether you have consulted the following sources for financial information in the past:",
        widget=forms.CheckboxSelectMultiple(
            choices=[
                ['1', 'Investment advisors and professionals'],
                ['2', 'Company and regulator website'],
                ['3', 'Blogs, forums, and social media'],
                ['4', 'Friends, family, and acquaintances'],
                ['5', 'Television, magazines, and newspapers'],
                ['6', 'Other sources'],
            ],
        )
    )

    FE4 = models.IntegerField(
        label = "Please provide an estimate of the number of days during an average week that you consult companies’ financial statements for financial information in an average week, for instance, through the company website or the SEC filing:"
    )

    FE5 = models.IntegerField(
        label = "Please provide an estimate of the number of days during an average week that you consume and consult economic and financial news (e.g., financial media, specialized online media, etc.):"
    )

    FE6 = models.StringField(
        blank=True,
        label="Please indicate whether you plan to consult the following sources for financial information in the future:",
        widget=forms.CheckboxSelectMultiple(
            choices=[
                ['1', 'Investment advisors and professionals'],
                ['2', 'Company and regulator website'],
                ['3', 'Blogs, forums, and social media'],
                ['4', 'Friends, family, and acquaintances'],
                ['5', 'Television, magazines, and newspapers'],
                ['6', 'Other sources'],
            ],
        )
    )

# Demographic Information

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
            [6, 'Africa']
        ]
    )

    employment = models.IntegerField(
        label = "Please select what best describes your current employment status",
        choices = [
            [1, "Working a full-time job for pay or profit (i.e., 35 hours a week or more)"],
            [2, "Working a part-time job for pay or profit (i.e., 1-34 hours a week)"],
            [3, "Working two or more part-time jobs for pay (totaling 35 hours or more per week)"],
            [4, "Unemployed and looking for work"],
            [5, "Unemployed and not looking for work"],
            [6, "With a job, but not temporary at work"],
            [7, "Retired"],
            [8, "Student"],
            [9, "Volunteer work"],
            [10, "I prefer not to say"]
        ]
    )

    education = models.IntegerField(
        label = "What is the highest level of education that you have completed?",
        choices = [
            [1, 'Less than High school (0-8 years)'],
            [2, 'Some High school (9-12 years, but did not graduate)'],
            [3, 'GED or High school equivalency'],
            [4, 'High school graduate'],
            [5, 'Vocational or trade school'],
            [6, '2-year College'],
            [7, '4-year College (BS, BA, or similar)'],
            [8, 'Some postgraduate (no degree)'],
            [9, 'Some postgraduate (MS, MA, PhD, MBA, MD, etc.)'],
            [10, 'I prefer not to say']
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
            [7, '40 years or more work experience.'],
        ]
    )

    english = models.IntegerField(
        label="Please rate your English on a percentage scale between 0 and 100.",
        min=0,
        max=100,
        blank=False,
        initial=None
    )

# Process Variables

    rd = models.IntegerField(
        label="To what extent was your decision to invest in the firms influenced by the amount of Research and Development (R&D) the firms did?",
        choices=Constants.DefinitelyChoices
    )

    purple = models.IntegerField(
        label = "To make sure you are paying attention, please select purple.",
        choices = [
            [1, 'Blue'],
            [2, 'Red'],
            [3, 'Purple'],
            [4, 'Yellow'],
            [5, 'Green']
        ]
    )

    ethical_rd = models.IntegerField(
        label = "I consider it unethical to manage taxes using R&D tax credits.",
        choices = Constants.AgreeChoices
    )

    ethical_ps = models.IntegerField(
        label = "I consider it unethical to manage taxes by shifting profits to other countries.",
        choices = Constants.AgreeChoices
    )

    politics = models.IntegerField(
        label = "Please indicate which political party best describes your political orientation.",
        choices = [
            [1, 'Democrats'],
            [2, 'Republicans'],
            [3, 'Other'],
            [4, 'Prefer not to say']
        ]
    )

    tax_advisor = models.IntegerField(
        label = "How often do you consult a tax advisor?",
        choices = [
            [1, 'Never'],
            [2, 'Very rarely'],
            [3, 'Rarely'],
            [4, 'Sometimes'],
            [5, 'Occasionally'],
            [6, 'Frequently'],
            [7, 'Very frequently']
        ]
    )

# End of HIT MTurk

    mturk = models.IntegerField(
        label = "How would you rate the difficulty of this HIT?",
        choices = [
            [1, 'Extremely easy'],
            [2, 'Moderately easy'],
            [3, 'Slightly easy'],
            [4, 'Neither easy nor difficult'],
            [5, 'Slightly difficult'],
            [6, 'Moderately difficult'],
            [7, 'Extremely difficult']
        ],
        blank=True
    )

    mturk_feedback = models.StringField(
        label = "Any comments or feedback for this HIT?",
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

# Investor Judgments

    islider = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
        )

    check_islider = models.FloatField(blank=True, initial=None)

    iinvest = models.IntegerField(
        label="Based on the information you just read, would you consider investing in Alophonica?",
        choices=Constants.DefinitelyChoices
        )

    consultother = models.StringField(
        blank=True,
        # label="Given the information you just read, would you still consult other sources of information before you decide about investing in Alophonica?",
        widget = forms.CheckboxSelectMultiple(
            choices=[
                [1, 'Investment advisors and professionals'],
                [2, 'Company and regulator websites'],
                [3, 'Blogs, forums, and social media'],
                [4, 'Friends, family, and acquaintances'],
                [5, 'Television, magazines, and newspapers'],
                [6, 'Annual reports and other financial disclosures'],
                [7, 'Other sources']
            ],
            )
        )

    islider2 = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
        )

    check_islider2 = models.FloatField(blank=True, initial=None)

    iinvest2 = models.IntegerField(
        label="Based on the information you just read, would you consider investing in Bellico?",
        choices=Constants.DefinitelyChoices
        )

    consultother2 = models.StringField(
        blank=True,
        label="Given the information you just read, would you still consult other sources of information before you decide about investing in Bellico?",
        widget=forms.CheckboxSelectMultiple(
            choices=[
                [1, 'Investment advisors and professionals'],
                [2, 'Company and regulator websites'],
                [3, 'Blogs, forums, and social media'],
                [4, 'Friends, family, and acquaintances'],
                [5, 'Television, magazines, and newspapers'],
                [6, 'Annual reports and other financial disclosures'],
                [7, 'Other sources']
            ],
        )
        )

    imarketslider = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=False),
        min=-100,
        initial=0,
        max=100,
    )
    check_imarketslider= models.FloatField(blank=True, initial=None)

    # Tax Ethicality

    alotax = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=False),
        min=-100,
        initial=None,
        max=100,
        )

    check_alotax = models.FloatField(blank=True, initial=None)

    beltax = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=False),
        min=-100,
        initial=None,
        max=100,
        )

    check_beltax = models.FloatField(blank=True, initial=None)