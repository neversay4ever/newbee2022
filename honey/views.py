from django.shortcuts import render
from django.core import serializers

from .models import HoneyCollector, HoneyIngredients, HoneyRefGenome, HoneySample

honey_collector = HoneyCollector.objects.all()
honey_ingredients = HoneyIngredients.objects.all()
honey_refgenome = HoneyRefGenome.objects.all()
honey_sample = HoneySample.objects.all()

def honey_home(request):
    return render(request, 'honey/honey_home.html', {'honey_collector': honey_collector, 
                'honey_ingredients': honey_ingredients, 
                'honey_refgenome':honey_refgenome,
                'honey_sample':honey_sample,
                })

