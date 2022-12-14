from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .models import Question

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_questions_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voing on question %s." % question_id)