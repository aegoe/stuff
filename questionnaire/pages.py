from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Q(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'reveal_info']


class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        return self.session.config['treatment']


class Results(Page):
    pass


page_sequence = [
    Q,
    ResultsWaitPage,
    Results
]
