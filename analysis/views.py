from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def check(request):

    return HttpResponse("ok", content_type='application/json')
