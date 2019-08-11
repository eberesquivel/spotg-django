from django.views.generic import TemplateView


class Parser(TemplateView):
    template_name = 'rgbtobgr/parser.html'
