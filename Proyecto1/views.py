from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    doc_externo=open("Z:/ProyectoDjango1/Proyecto1/Proyecto1/plantillas/primerplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Hasta luego alumnos de Django')

def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento= """<html>
    <body>
    <h1>
    Fecha y ahora Actual %s
    </h1>
    </body>
    </html>"""""% fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, anio):
    
    periodo=anio-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(anio, edadFutura)

    return HttpResponse(documento)

