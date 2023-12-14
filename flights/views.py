from django.http.response import HttpResponse , JsonResponse
from .models import flight,Airport
def list(request):
    flights=flight.objects.all()
    flight_list=[]
    for item in flights:
        dec={
            "origin":item.origin.Name,
            "flight_number":item.flight_number

        }
        flight_list.append(dec)
    return HttpResponse(flight_list)

def list2(request):
    air=Airport.objects.all()
    air_list=[]
    for item in air:
        dic_air={
            "Name": item.Name,
            "No": item.No,
            "City":item.City,
            "Address":item.Address,
            "Phone_Number":item.Phone_Number,
            "open_time":item.open_time,
            "close_time":item.close_time
        }
        air_list.append(dic_air)
    return HttpResponse(air_list)

