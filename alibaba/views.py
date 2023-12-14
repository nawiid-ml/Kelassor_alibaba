from django.http.response import HttpResponse , JsonResponse
def welcome (request):
    return HttpResponse ("welcome to alibab")
def about (request):
    return HttpResponse ("here is about")
def contact(request):
    return HttpResponse ("this is contact")

    