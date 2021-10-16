from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include('pizza_api.urls')), #Pizza_api urls included in project url
]
