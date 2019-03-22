from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    pass

class Send(Page):
    form_model = 'group'
    form_fields = ['amount_sent']

    def is_displayed(self):
        return self.player.role() == 'trustor'

    def before_next_page(self):
        self.group.amount_sent_multiplied = self.group.amount_sent * Constants.multiplier


class WaitPageP1(WaitPage):

    def after_all_players_arrive(self):
        pass


class SendBack(Page):
    form_model = 'group'
    form_fields = ['amount_sent_back']

    def amount_send_back_max(self):
        return self.group.amount_sent_multiplied

    def is_displayed(self):
        return self.player.role() == 'trustee'


class WaitPageP2(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Send,
    WaitPageP1,
    SendBack,
    WaitPageP2,
    Results
]
