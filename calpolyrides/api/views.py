from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Item
from api.models import RideRequestPost
from api.models import SearchFilter
from api.serializers import ItemSerializer
from api.serializers import RideRequestPostSerializer
from api.serializers import SearchFilterSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #def list(self, request):   inherets this from modelviewset

class RideRequestPostViewSet(viewsets.ModelViewSet):
    queryset = RideRequestPost.objects.all()
    serializer_class = RideRequestPostSerializer

class SearchFilterViewSet(viewsets.ModelViewSet):
    queryset = SearchFilter.objects.all()
    serializer_class = SearchFilterSerializer