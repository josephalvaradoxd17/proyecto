from django import forms

from ppp.models import Periodo

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'