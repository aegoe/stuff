from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_game'
    players_per_group = 3
    num_rounds = 5

    endowment = c(100)
    multiplier = 2
    lb = 50
    ub = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        for i in self.get_players():
            if self.round_number == 1:
                if self.session.config.get('hetero_endowment'):
                    i.endowment = random.randint(Constants.lb, Constants.ub)
                    #i.endowment = random.choice([0, 50, 100)
                else:
                    i.endowment = Constants.endowment
            else:
                i.endowment = i.in_round(1).endowment
            # i.endowment = Constants.endowment


class Group(BaseGroup):
    group_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    average_contribution = models.CurrencyField()

    def set_payoffs(self):
        self.group_contribution = sum([p.individual_contribution for p in self.get_players()])
        self.individual_share = self.group_contribution * Constants.multiplier / Constants.players_per_group
        self.average_contribution = self.group_contribution / Constants.players_per_group
        for p in self.get_players():
            p.payoff = p.endowment - p.individual_contribution + self.individual_share


class Player(BasePlayer):
    endowment = models.CurrencyField()
    individual_contribution = models.CurrencyField(label = "How much you wanna contribute dawg?",
                                                   min = 0,
                                                   )
