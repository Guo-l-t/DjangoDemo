from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Birthday
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def query_to_dic(query):
    dic = model_to_dict(query)


def index(request):
    bir = Birthday.objects.all()

    return render(request, 'birthday/index.html', {'bir': bir})


def add(request):
    name = request.GET['name']
    yinyang = request.GET['yinyang']
    if yinyang == 'yin':
        yinyang = '01'
    else:
        yinyang = '02'
    year = request.GET['year']
    mouth = request.GET['mouth']
    day = request.GET['day']
    bir = Birthday(name=name, state=yinyang, year=year, mouth=mouth, day=day)
    bir.save()
    return HttpResponseRedirect("/birthday/")


# def vote(request, question_id):
#     return HttpResponse("vote   You're voting on question %s." % question_id)
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})