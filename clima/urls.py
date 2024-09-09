from django.urls import path
from .views import index, weather_results

urlpatterns = [
    path('', index, name='index'),
    path('weather/<str:city>/', weather_results, name='weather_results'),
]
