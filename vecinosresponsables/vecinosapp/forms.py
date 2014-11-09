# -*- coding: utf-8 -*-
from vecinosapp.models import Aviso
from django.forms import ModelForm


class AvisoForm(ModelForm):
    class Meta:
        model = Aviso
        exclude = ('resuelto',
                    'latitud',
                    'longitud',
                    'fecha',)