from django.shortcuts import render, HttpResponse

#def index(request):
#    return HttpResponse("Hello world")

def index(request):
    my_dict= {'insert_me':"Hello, i'm from views.py!"}
    return render(request, 'first_app/index.html', context=my_dict)

def help(request):
    my_dict= {'insert_me':"Ready to help you from views.py!"}
    return render(request, 'first_app/help.html', context=my_dict)