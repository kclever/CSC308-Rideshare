from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Item
from .models import Account
from .serializers import ItemSerializer, AccountSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #def list(self, request):   inherets this from modelviewset

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

