from django.urls import path
from pizza_api import views




urlpatterns = [
    path('create/', views.PizzaCreateView.as_view()), # create url for pizza api
    path('list/', views.PizzaListView.as_view()), # list url for pizza api
    path('edit-delete/<int:pk>/', views.PizzaUpdateDeleteViews.as_view()), # update and delete url for pizza api

]
