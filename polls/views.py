from django.shortcuts import render
from .models import Question
# Create your views here.
from django.http import HttpResponse
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")
    return HttpResponse("Hello, world .You're at the polls index.")
def detail(request):
    return HttpResponse("Hello, world .You're at the polls index.")
def results(request,questions_id):
    response="You're looking at the results of question %s"
    return HttpResponse(response % questions_id)
def vote(request,questions_id):
    return HttpResponse("You're voting on question %s" % questions_id)
