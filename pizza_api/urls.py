from django.urls import path
from pizza_api import views




urlpatterns = [
    path('create/', views.PizzaCreateView.as_view()), # create endpoint for pizza api
    path('list/', views.PizzaListView.as_view()), # list endpoint for pizza api
    path('edit-delete/<int:pk>/', views.PizzaUpdateDeleteViews.as_view()), # update and delete endpoint for pizza api

]
