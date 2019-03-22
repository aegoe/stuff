from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    cases = ['greedy', 'random', 'generous']

    def play_round(self):
        if self.round_number == 1:
            yield pages.Instructions
        if self.case == 'greedy':
            contribution = 0
        elif self.case == 'random':
            contribution = random.randint(0, self.player.endowment)
        else:
            contribution = self.player.endowment
        yield pages.Contribution, {'individual_contribution': contribution}
        yield pages.Results

