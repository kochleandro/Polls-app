from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404


# def index(request):
#     return HttpResponse("Hola mundo. Estás en el índice de encuestas..")

# def detail(request, question_id):
#     return HttpResponse("Estás viendo la pregunta %s." % question_id)


def results(request, question_id):
    response = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Estás votando la pregunta %s." % question_id)

# def index(request):
#     #Pide el orden de los resultados, las Questions
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     #Define la variable "Template" y le carga el template de la crapeta template/polls
#     template = loader.get_template("polls/index.html")
#     #El contexto es un diccionario que relaciona los nombres de variables de plantillas con objetos Python.
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #Lo mismo pero mas resumido, define el contexto
    context = {"latest_question_list": latest_question_list}
    #Aca carga la plantilla y le mete el contexto, todo con render
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})