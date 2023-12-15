from django.http.response import HttpResponse , JsonResponse

def list(request):
    dic={
    "Train_Name":"Shahin",
    "Origin":"Tehran",
    "Destination":"shiraz",
    "Date_Of_Departure":8,
    "Return_Of_Departure":11
    }
    return JsonResponse(dic,safe=False)
