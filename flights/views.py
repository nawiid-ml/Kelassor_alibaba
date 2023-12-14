from django.http.response import HttpResponse , JsonResponse
def list(request):
    flight_dic={
        "flight number ":458,
        "name":"first class",
        "seat ":2565,
        "price":5698568
        }
    return JsonResponse(flight_dic)