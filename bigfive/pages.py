from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    def get_progress(self):
        totpages = self.participant._max_page_index
        curpage = self.participant._index_in_pages
        return f"{curpage / totpages * 100:.0f}"


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender']


class BigFive(Page):
    form_model = 'player'
    form_fields = ['life']


page_sequence = [
    Demographics,
    BigFive,
]
