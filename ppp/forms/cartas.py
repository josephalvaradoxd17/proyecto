from django import forms

from ppp.models import Carta, HistorialCarta

class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = '__all__'

class Alumno_CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        exclude = ['estado','secretaria']
        widgets = {
            'alumno': forms.MultipleHiddenInput(),
        }

class HistorialCartaForm(forms.ModelForm):
    class Meta:
        model = HistorialCarta
        fields = ['carta','observacion','archivo']
        widgets = {
            'carta': forms.HiddenInput(),
            'observacion': forms.Textarea(),
        }