from django.shortcuts import render, get_object_or_404

from actividad.models import Actividad


def actividad(request, id_actividad):
    registro = get_object_or_404(Actividad, pk=id_actividad)
    return render(request, "actividad/formato.html", {"registro": registro})
