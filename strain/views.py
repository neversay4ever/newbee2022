from django.shortcuts import render
from django.core import serializers

from .models import StrainAll

strain_all = StrainAll.objects.all()

def strain_home(request):
    return render(request, 'strain/strain_home.html', {'strain_all': strain_all, })

def strain_single(request, strain_id):
    # breed_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:{breed_data}'
    # Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:北方中蜂-Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:海南中蜂
    strain = StrainAll.objects.filter(strain_id=strain_id)
    print(strain)
    return render(request, 'strain/strain_single.html', {'strains': strain})

    