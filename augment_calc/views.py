from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ReporteForm
from .models import *


class AugmentCalc(TemplateView):
    template_name = 'augment_calc/inicio.html'

    def get_context_data(self, **kwargs):
        context = super(AugmentCalc, self).get_context_data()
        activo = Augment_Type.objects.get(id=1)
        chance = Augment_Type.objects.get(id=2)
        pasivo = Augment_Type.objects.get(id=3)
        context['lista_todos'] = Augment_Skill.objects.all()
        context['lista_activos'] = Augment_Skill.objects.filter(type=activo)
        context['lista_chances'] = Augment_Skill.objects.filter(type=chance)
        context['lista_pasivos'] = Augment_Skill.objects.filter(type=pasivo)
        return context


def reporte(request):
    todos_los_aumentos = Augment_Skill.objects.all()
    lista_aumentos = []
    for elemento in todos_los_aumentos:
        lista_aumentos.append(elemento.short_format)

    if request.POST:
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            # Limpiar el formulario
            form = ReporteForm()
            reporte_guardado = True
            return render(request, 'augment_calc/reporte.html', {'lista_aumentos': lista_aumentos,
                                                                 'form': form,
                                                                 'reporte_guardado': reporte_guardado})
    else:
        form = ReporteForm()

    return render(request, 'augment_calc/reporte.html', {'lista_aumentos': lista_aumentos,
                                                         'form': form})
