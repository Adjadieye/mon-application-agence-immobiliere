from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Ajoutez d'autres URLs selon les besoins
]