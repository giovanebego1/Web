from re import template
from django.shortcuts import render, HttpResponse
from django.template import loader
from . import forms

#def index(request):
#    return HttpResponse("Hello world")

def index(request):
    my_dict= {'insert_me':"Hello, i'm from views.py!"}
    return render(request, 'first_app/index.html', context=my_dict)

def help(request):
    my_dict= {'insert_me':"Ready to help you from views.py!"}
    return render(request, 'first_app/help.html', context=my_dict)

def web(request):
    my_dict={'insert_me': "Ready to show the Web page from views.py!"}
    return render(request, "first_app/web.html", context=my_dict)

def calculadora(request):
    my_dict={'insert_me': "Ready to show the calculator from viwes.py!"}
    return render(request, "first_app/calculadora.html", context=my_dict)

def first_form(request):
    form = forms.first_form()
    return render(request, 'first_form.html',{'form':form})