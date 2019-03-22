from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribution(Page):
    form_model = 'player'
    form_fields = ['individual_contribution']

    def vars_for_template(self):
        return {'mylabel': f'How much do you want to contribute? Choose anything between 0 and {self.player.endowment}'}

    def individual_contribution_max(self):
        return self.player.endowment


class WaitPage1(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Contribution,
    WaitPage1,
    Results,
]
