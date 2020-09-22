import graphene
from graphene_django import DjangoObjectType
from app01.models import Shop
from django.contrib.gis.geos import Point,Polygon
from django.contrib.gis.geos import GEOSGeometry

class ShopType(DjangoObjectType):
    class Meta:
        model =Shop
        fields = '__all__'
    
class Query(graphene.ObjectType):
    area_shops =graphene.List(ShopType)
    area_of_shop = graphene.Field(ShopType,name= graphene.String())

    def resolve_area_shops(self,root,info,**kwargs):
        return Shop.objects.all()
    
    def reolve_area_of_shops(self,root,info,name):
        return Shop.objects.get(name=name)

schema = graphene.Schema(query=Query)

    