from django.http import HttpResponse
from django.shortcuts import render

def print_hello(request):
    return HttpResponse("Hello!")

def print_info(request):
    return HttpResponse("I create a first branch!")