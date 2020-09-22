from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Shop
from django.contrib.gis.geos import Point
# Create your views here.
def home_view(request):
    srid=4326
    
    # s1 = Shop('Shop_name',Point([5,4]),(((0,0),(3,5),(4,6),(7,9),(0,0))),'Address_of_shop','City_of_shop')
    # s1.save()
    p1 =Point([4,5])
    s1 = Shop(name="Jigar_point",polygonn=p1)
    s1.save()
    print("save success")
    return HttpResponse("This is home view")



