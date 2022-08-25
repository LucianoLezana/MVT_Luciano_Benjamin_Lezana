import imp
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from familiares.models import Familiares


def Saludo(request):
    return HttpResponse("Hola soy un mensaje de la pagina creada por Luciano")


def probar_familiares(request):
    queryset = Familiares.objects.all()
    dic = {'familiares': queryset}
    template = loader.get_template('template_1.html')
    document_html = template.render(dic)
    return HttpResponse(document_html)