from django.shortcuts import render
from pizza_api.serializers import PizzaSerializer
from pizza_api.models import Pizza
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters


class PizzaCreateView(CreateAPIView):
    """
    Create API View class created for creates pizza.
    
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaListView(ListAPIView):
    """
    List API View class created for see list of all information
    about pizza.
    
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = (filters.DjangoFilterBackend,) # Django Filter Backends
    filterset_fields = ['pizza_type', 'pizza_size'] # Filter should applied on these fields


class PizzaUpdateDeleteViews(RetrieveUpdateDestroyAPIView):
    """
    Retrieve Update Destroy API class created for edit and delete
    pizza by pk.
    
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer