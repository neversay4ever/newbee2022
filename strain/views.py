from django.shortcuts import render
from django.core import serializers

from .models import StrainAll

strain_all = StrainAll.objects.all()

def strain_home(request):
    return render(request, 'strain/strain_home.html', {'strain_all': strain_all, })

