from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'trust_game'
    players_per_group = 2
    num_rounds = 1

    endowment = c(100)
    multiplier = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    amount_sent = models.CurrencyField()
    amount_sent_multiplied = models.CurrencyField()
    amount_sent_back = models.IntegerField()

    def set_payoffs(self):
        trustor = self.get_player_by_role('trustor')
        trustee = self.get_player_by_role('trustee')

        trustor.payoff = Constants.endowment - self.amount_sent + self.amount_sent_back
        trustee.payoff = Constants.endowment + self.amount_sent_multiplied - self.amount_sent_back


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'trustor'
        else:
            return 'trustee'

    def other(self):
        return self.get_others_in_group()[0]
