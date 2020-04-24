from django.forms import *
from .models import *


class ReporteForm(ModelForm):
    class Meta:
        model = Reporte
        fields = ['augment_skill_id', 'attribute_description']
        widgets = {
            'augment_skill_id': TextInput(attrs={'class': 'autocomplete validate'}),
            'attribute_description': Textarea(attrs={'class': 'materialize-textarea validate'})
        }
