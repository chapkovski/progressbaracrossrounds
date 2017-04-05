from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def progress(p):
    #lazy way:
    progressrel = p._index_in_pages/p.player.participant._max_page_index*100
    # right way:
    curpageindex = page_sequence.index(type(p))+1
    progressrel = ((p.round_number-1)*pages_per_round+curpageindex)/tot_pages*100
    return progressrel

class Demographics(Page):
    form_model = models.Player
    form_fields = [
                   'gender']

    def vars_for_template(self):
        return{
               'progressrel':progress(self)
               }

class BigFive(Page):
    form_model = models.Player
    form_fields = ['life']

    def vars_for_template(self):
        return{
               'progressrel':progress(self)
               }

page_sequence = [
    Demographics,
    BigFive,
]
#right way
pages_per_round = len(page_sequence)
tot_pages = pages_per_round * Constants.num_rounds
