from django import forms
from .models import Game

class GameForm(forms.ModelForm):

    class Meta:
        model = Game

        fields = [
        'id',
        'name',
        'platform',
        'genre',
        'publisher',
        'release_year',
        'na_sales',
        'eu_sales',
        'jp_sales',
        'other_sales',
        'global_sales'
        ]