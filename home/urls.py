from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('process', process, name='process'),
    path('<str:url>', get_url, name='get_url')
]
