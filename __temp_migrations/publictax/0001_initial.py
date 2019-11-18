# Generated by Django 2.2.4 on 2019-11-16 18:50

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publictax_group', to='otree.Session')),
            ],
            options={
                'db_table': 'publictax_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publictax_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'publictax_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('treat', otree.db.models.StringField(max_length=10000, null=True)),
                ('accept_conditions', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('Instr1', otree.db.models.IntegerField(choices=[[1, 'True'], [2, 'False']], null=True)),
                ('Instr2', otree.db.models.IntegerField(choices=[[1, 'True'], [2, 'False']], null=True)),
                ('Instr3', otree.db.models.IntegerField(choices=[[1, 'True'], [2, 'False']], null=True)),
                ('timer_id', otree.db.models.StringField(blank=True, max_length=10000, null=True)),
                ('FL1', otree.db.models.IntegerField(choices=[[1, 'More than $102'], [2, 'Exactly $102'], [3, 'Less than $102'], [4, "I don't know"]], null=True, verbose_name='Suppose you had $100 in a savings account and the interest rate was 2% per year. After 5 years, how much do you think you would have in the account if you left the money to grow?')),
                ('FL2', otree.db.models.IntegerField(choices=[[1, 'More than $200'], [2, 'Exactly $200'], [3, 'Less than $200'], [4, "I don't know"]], null=True, verbose_name='Suppose you had $100 in a savings account and the interest rate is 20% per year and you never withdraw money or interest payments. After 5 years, how much would you have on this account in total?')),
                ('FL3', otree.db.models.IntegerField(choices=[[1, 'More than today'], [2, 'Exactly the same as today'], [3, 'Less than today'], [4, "I don't know"]], null=True, verbose_name='Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per year. After 1 year, how much would you be able to buy with the money in this account?')),
                ('FL4', otree.db.models.IntegerField(choices=[[1, 'My friend'], [2, 'His sibling'], [3, 'They are equally rich'], [4, "I don't know"]], null=True, verbose_name='Assume a friend inherits $10,000 today and his sibling inherits $10,000 three years from now. Assume both your friend and his sibling do not spend the $10,000. Who is richer because of the inheritance?')),
                ('FL5', otree.db.models.IntegerField(choices=[[1, 'More than today'], [2, 'Exactly the same'], [3, 'Less than today'], [4, "I don't know"]], null=True, verbose_name='Suppose that in the year 2020, your income has doubled, and prices of all goods have doubled too. In 2020, how much will you be able to buy with your income?')),
                ('FL6', otree.db.models.IntegerField(choices=[[1, 'Savings accounts'], [2, 'Individual shares and stocks'], [3, 'Debt securities and bonds'], [4, "I don't know"]], null=True, verbose_name='Which of the following financial assets typically grant you the highest return over a long period of time (e.g., 10-20 years)?')),
                ('FL7', otree.db.models.IntegerField(choices=[[1, 'They rise'], [2, 'They fall'], [3, 'They stay the same'], [4, 'I do not know']], null=True, verbose_name='If the interest rate drops, what happens to bond prices?')),
                ('FL8', otree.db.models.IntegerField(choices=[[1, 'It is less likely to experience any difficulty with its creditors compared to other firms in the industry'], [2, 'It has less liquidity than other firms in the industry'], [3, 'It will be viewed as having relatively high creditworthiness'], [4, 'It has greater than average financial risk when compared to other firms in the industry'], [5, "I don't know"]], null=True, verbose_name='Compared to similar firms in the same industry, a company uses more borrowed money to finance its operations. Which of the following statements is most likely to be true for the company?')),
                ('FL9', otree.db.models.IntegerField(choices=[[1, 'Increasing short-term assets while decreasing short-term liabilities'], [2, 'Increasing short-term assets while increasing short-term liabilities'], [3, 'Reducing short-term assets, increasing short-term liabilities, and reducing long-term liabilities'], [4, 'Replacing short-term liabilities with equity'], [5, "I don't know"]], null=True, verbose_name='Which of the following activities would most likely result in an increased risk of the firm being unable to repay borrowed funds?')),
                ('FL10', otree.db.models.IntegerField(choices=[[1, 'He owns a part of firm B'], [2, 'He has lent money to firm B'], [3, "He is liable for firm B's debts"], [4, 'None of the above'], [5, "I don't know"]], null=True, verbose_name='Which of the following statements is correct? If somebody buys a bond of firm B:')),
                ('rd', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='Alophonica’s innovativeness influenced my decision about it paying its fair share of taxes')),
                ('australia_check', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='The tax authorities of Olmeos disclosed information about Alophonica’s operations in Olmeos.')),
                ('cbc_check', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='The tax authorities of Olmeos disclosed information about Alophonica’s operations in other countries than Olmeos.')),
                ('fair_rd', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='It is fair to lower taxes using investment tax credits.')),
                ('fair_ps', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='It is fair to lower taxes by shifting profits to countries with lower statutory tax rate such as Hingland.')),
                ('fair_more', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='It is fairer to lower taxes by shifting profit than by using investment tax credits.')),
                ('fair_ptd', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name="The information disclosed by Olmeos' tax authorities influenced my decision about Alophonica paying its fair share of taxes.")),
                ('fair_report', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name="The information in Alophonica's financial report influenced my decision about Alophonica paying its fair share of taxes.")),
                ('gender', otree.db.models.IntegerField(choices=[[1, 'Male'], [2, 'Female'], [3, 'Other'], [4, 'I prefer not to say']], null=True, verbose_name='Please select your gender.')),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='Please enter your age.')),
                ('nationality', otree.db.models.IntegerField(choices=[[1, 'North-America'], [2, 'Central and South-America'], [3, 'Asia'], [4, 'Europe'], [5, 'Australia and Oceania'], [6, 'Africa'], [7, 'I prefer not to say']], null=True, verbose_name='Please select your region of residence.')),
                ('employment', otree.db.models.IntegerField(choices=[[1, 'Working full-time'], [2, 'Working part-time'], [3, 'Unemployed and looking for work'], [4, 'Unemployed and not looking for work'], [5, 'Retired'], [6, 'Student'], [7, 'I prefer not to say']], null=True, verbose_name='Please select what best describes your current employment status.')),
                ('education', otree.db.models.IntegerField(choices=[[1, 'Less than High school'], [2, 'High school'], [3, 'Vocational or trade school'], [4, '2-year College'], [5, '4-year College (BS, BA, or similar)'], [6, 'Postgraduate (MS, MA, PhD, MBA, MD, etc.)'], [7, 'I prefer not to say']], null=True, verbose_name='What is the highest level of education that you have completed?')),
                ('workexperience', otree.db.models.IntegerField(choices=[[1, 'I do not have work experience.'], [2, 'Less than 5 year work experience.'], [3, 'Between 5 and less than 10 years of work experience'], [4, 'Between 10 and less than 20 years work experience.'], [5, 'Between 20 and less than 30 years work experience.'], [6, 'Between 30 and less than 40 years work experience.'], [7, '40 years or more work experience.']], null=True, verbose_name='Please indicate your work experience. All jobs count, including part-time and volunteer work.')),
                ('english', otree.db.models.IntegerField(null=True, verbose_name='Please rate your English on a percentage scale between 0 and 100.')),
                ('politics', otree.db.models.IntegerField(choices=[[1, 'Democrats'], [2, 'Republicans'], [3, 'Other'], [4, 'Prefer not to say']], null=True, verbose_name='Please indicate which political party best describes your political orientation.')),
                ('tax_advisor', otree.db.models.IntegerField(choices=[[1, 'Never'], [2, 'Very rarely'], [3, 'Rarely'], [4, 'Sometimes'], [5, 'Occasionally'], [6, 'Frequently'], [7, 'Very frequently']], null=True, verbose_name='How often do you consult a tax advisor, both privately or as part of your job?')),
                ('TA_1', otree.db.models.IntegerField(choices=[[1, '1: Never Justified'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10: Always Justified']], null=True, verbose_name='To what extent do you think claiming state benefits to which one is not entitled is justified?')),
                ('TA_2', otree.db.models.IntegerField(choices=[[1, '1: Never Justified'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10: Always Justified']], null=True, verbose_name='To what extent do you think that cheating on taxes if one had the chance is justified?')),
                ('TA_3', otree.db.models.IntegerField(choices=[[1, '1: Never Justified'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10: Always Justified']], null=True, verbose_name='To what extent do you think that avoiding taxes by using legal means if given the chance is justified?')),
                ('Function', otree.db.models.IntegerField(choices=[[1, 'General Management'], [2, 'Operations'], [3, 'Finance/Accounting'], [4, 'Marketing/Sales'], [5, 'Human Resources'], [6, 'R&D'], [7, 'Other'], [8, 'None, I am unemployed']], null=True, verbose_name='In which function of your organization do you currently work (please check one)?')),
                ('Industry', otree.db.models.IntegerField(choices=[[1, 'Mining/Oil/Gas'], [2, 'Construction'], [3, 'Transportation'], [4, 'Manufacturing'], [5, 'Retail'], [6, 'Financial Services'], [7, 'Health Care'], [8, 'Other Services'], [9, 'Not-For-Profit'], [10, 'Government'], [11, 'Other'], [12, 'None, I am unemployed']], null=True, verbose_name='In which industry does your firm primarily conduct business?')),
                ('fin_exp', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='I have experience with conducting trades and transactions with financial assets such as debt securities, bonds, shares, financial funds, and derivatives.')),
                ('fin_own', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='I have indirectly or directly owned financial assets such as debt securities, bonds, shares, mutual or pension funds, and derivatives.')),
                ('tax_exp', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name='I have been involved in making tax management policies and setting out tax strategies for firms.')),
                ('tax_an', otree.db.models.IntegerField(choices=[[1, 'Disagree strongly'], [2, 'Disagree moderately'], [3, 'Disagree a little'], [4, 'Neither agree nor disagree'], [5, 'Agree a little'], [6, 'Agree moderately'], [7, 'Agree strongly']], null=True, verbose_name="I have experience with analyzing and evaluating firms' tax management strategies and policies.")),
                ('i_judge_1', otree.db.models.FloatField(default=0, null=True)),
                ('check_i_judge_1', otree.db.models.FloatField(blank=True, null=True)),
                ('i_judge_2', otree.db.models.FloatField(default=0, null=True)),
                ('check_i_judge_2', otree.db.models.FloatField(blank=True, null=True)),
                ('i_judge_3', otree.db.models.FloatField(default=0, null=True)),
                ('check_i_judge_3', otree.db.models.FloatField(blank=True, null=True)),
                ('i_market', otree.db.models.FloatField(default=0, null=True)),
                ('check_i_market', otree.db.models.FloatField(blank=True, null=True)),
                ('alotax', otree.db.models.FloatField(null=True)),
                ('check_alotax', otree.db.models.FloatField(blank=True, null=True)),
                ('mturk', otree.db.models.IntegerField(blank=True, choices=[[1, 'Extremely easy'], [2, 'Moderately easy'], [3, 'Slightly easy'], [4, 'Neither easy nor difficult'], [5, 'Slightly difficult'], [6, 'Moderately difficult'], [7, 'Extremely difficult']], null=True, verbose_name='How difficult was this HIT?')),
                ('mturk_feedback', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Do you have any feedback for us or anything you would like to say to us')),
                ('mturk_motivation', otree.db.models.IntegerField(choices=[[1, 'Extremely unmotivated'], [2, 'Very unmotivated'], [3, 'Unmotivated'], [4, 'Neutral'], [5, 'Motivated'], [6, 'Very motivated'], [7, 'Extremely motivated']], null=True, verbose_name='How motivated were you during this HIT?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='publictax.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publictax_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publictax_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publictax.Subsession')),
            ],
            options={
                'db_table': 'publictax_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publictax.Subsession'),
        ),
    ]
