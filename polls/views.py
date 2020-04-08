from django.core import serializers
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Question, Employee


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
    return HttpResponse("You're looking at question %s." % question_id)


def jdata(request):
    data = list(Employee.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def jdata2(request):
    qs = Employee.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')
