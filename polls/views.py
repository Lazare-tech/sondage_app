from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello,world.you're the polls index")

#detail
def detail(request,question_id):
    return HttpResponse("You are looking at question %s." % question_id)

#resultat
def results(request,question_id):
    response="You are looking at results for question %s."
    return HttpResponse(response % question_id)

#vote
def vote(request,question_id):
    return HttpResponse("You are voting on question %s." % question_id)