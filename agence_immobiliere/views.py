from django.shortcuts import render
from .models import Propriete

def home(request):
    proprietes = Propriete.objects.all()
    return render(request, 'index.html', {'proprietes': proprietes})

# Ajoutez d'autres vues selon les besoins
