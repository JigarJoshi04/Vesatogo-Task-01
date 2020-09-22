from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Shop
from django.contrib.gis.geos import Point,Polygon
from django.contrib.gis.geos import GEOSGeometry
# Create your views here.
def home_view(request):
    srid=4326
    
    # s1 = Shop('Shop_name',Point([5,4]),(((0,0),(3,5),(4,6),(7,9),(0,0))),'Address_of_shop','City_of_shop')
    # s1.save()
    p2 =Point([0,0])
    # s1 = Shop(name="Jigar_point",polygonn=p1)
    # s1.save()
    # print("save success")
    # p1 = Polygon(((4,4),(5,2),(6,6),(4,4)))
    p1 = GEOSGeometry('POLYGON((-1 -1, -1 1 ,1 1, 1 -1, -1 -1))') 
    print("We are seeing something: ",p2.within(p1))
    s1 = Shop(name="Jigar_polygon",polygonn=p1)
    s1.save()
    print("save success")
    return HttpResponse("This is home view")

def reading(request):
    return HttpResponse("Check the console")



