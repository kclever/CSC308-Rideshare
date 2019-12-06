from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Item
from api.models import RideRequestPost
from api.serializers import ItemSerializer
from api.serializers import RideRequestPostSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #def list(self, request):   inherets this from modelviewset

class RideRequestPostViewSet(viewsets.ModelViewSet):
    queryset = RideRequestPost.objects.all()
    serializer_class = RideRequestPostSerializer

