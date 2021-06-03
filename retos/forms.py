from django import forms
from django.db.models import fields
from django.http import request
from .models import *
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import HiddenInput


class empleados_Form(forms.ModelForm):

    class Meta:
        model = Empleados
        fields = ['nombre', 'apellido', 'telefono',
                  'fecha_nacimiento', 'email']
        date = forms.DateField(
            widget=DatePickerInput(format='%m/%d/%Y')
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class tipo_reto_Form(forms.ModelForm):
    class Meta:
        model = Tipo_retos
        fields = "__all__"


class Cliente_Form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {'slug': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['Cliente_codigo'].widget.attrs['readonly'] = True


class Cli_retos_art_Form(forms.ModelForm):

    class Meta:
        model = Cli_retos_art
        fields = ['n_ticket', 'cliente_reto',
                  'images']
        # fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hide_condition = kwargs.pop('hide_condition', None)
        if hide_condition:
            self.fields['fecha_alta'].widget = HiddenInput()

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
