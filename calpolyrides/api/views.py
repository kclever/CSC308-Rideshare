from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import RideOfferPost
from api.models import RideRequestPost
from api.models import Search
from api.models import Filter
from api.serializers import RideOfferPostSerializer
from api.serializers import RideRequestPostSerializer
from api.serializers import SearchSerializer
from api.serializers import FilterSerializer
from django_filters import rest_framework as filters

# Create your views here.

class RideOfferPostFilter(filters.FilterSet):
    class Meta:
        model = RideOfferPost
        fields = {
            'from_u' : ['icontains'],
            'to_u' : ['icontains'],
            'when_u' : ['lte', 'gte'],
            'cost_u' : ['lte'],
        }

class RideOfferPostViewSet(viewsets.ModelViewSet):
    queryset = RideOfferPost.objects.all()
    serializer_class = RideOfferPostSerializer
    filterset_class = RideOfferPostFilter
    #def list(self, request):   inherets this from modelviewset

class RideRequestPostFilter(filters.FilterSet):
    class Meta:
        model = RideRequestPost
        fields = {
            'from_u' : ['icontains'],
            'to_u' : ['icontains'],
            'when_u' : ['lte', 'gte'],
        }

class RideRequestPostViewSet(viewsets.ModelViewSet):
    queryset = RideRequestPost.objects.all()
    serializer_class = RideRequestPostSerializer
    filterset_class = RideRequestPostFilter

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer