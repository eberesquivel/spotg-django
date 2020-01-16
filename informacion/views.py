import json
import urllib

from django.views.generic import TemplateView


class Inicio(TemplateView):
    template_name = 'informacion/inicio.html'


class Pago(TemplateView):
    template_name = 'informacion/pago.html'


class Servicios(TemplateView):
    template_name = 'informacion/servicios.html'


class Donacion(TemplateView):
    template_name = 'informacion/donacion.html'


class Comentarios(TemplateView):
    template_name = 'informacion/comentarios.html'


class Foro(TemplateView):
    template_name = 'foro_rss/reynaldev.html'

    def get_context_data(self, **kwargs):
        context = super(Foro, self).get_context_data()
        # Se usa https://rss2json.com para consultar el XML del foro 
        r = urllib.request.urlopen("https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.reddit.com%2Fr%IoT")
        # Se carga en JSON
        data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
        # Solo se llaman los items y pasan al contexto
        context['ultimos_temas'] = data['items']

        # Esta es la forma mas sencilla, pero pythonanywhere no me permite usarla directamente
        # context['ultimos_temas'] = feedparser.parse("https://l2devsadmins.net/reynaldev/index.php?action=.xml;type=rss")
        return context


class Faqs(TemplateView):
    template_name = 'informacion/faqs.html'

class Mapa(TemplateView):
    template_name = 'rgbtobgr/parser.html'

class Locacion(TemplateView):
    template_name = 'informacion/locacion.html'
