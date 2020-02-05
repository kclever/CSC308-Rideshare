from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Item
from api.models import RideRequestPost
from api.models import Search
from api.models import Filter
from api.serializers import ItemSerializer
from api.serializers import RideRequestPostSerializer
from api.serializers import SearchSerializer
from api.serializers import FilterSerializer
from django_filters import rest_framework as filters

# Create your views here.

class RideOfferPostFilter(filters.FilterSet):

    class Meta:
        model = Item
        fields = {
            'from_u' : ['icontains'],
            'to_u' : ['icontains'],
            'when_u' : ['lte', 'gte'],
            'cost_u' : ['lte'],
        }

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_class = RideOfferPostFilter
    #def list(self, request):   inherets this from modelviewset

class RideRequestPostViewSet(viewsets.ModelViewSet):
    queryset = RideRequestPost.objects.all()
    serializer_class = RideRequestPostSerializer

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer