from django.shortcuts import render,redirect
from django.core import serializers

from .models import StrainAll



def strain_home(request):
    strain_all = StrainAll.objects.all()
    return render(request, 'strain/strain_home.html', {'strain_all': strain_all, })

def strain_single(request, strain_id):
    # breed_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:{breed_data}'
    # Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:北方中蜂-Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:海南中蜂
    strain = StrainAll.objects.filter(strain_id=strain_id)
    return render(request, 'strain/strain_single.html', {'strains': strain})


from .models import StrainOrigin, Taxonomy, Sequencing16s, GenomeInfo,Isolate, Storage, StrainAll

def strain_data_combine(request):
    strain_origin_data = StrainOrigin.objects.all()
    for x in strain_origin_data.values():
        strain_id = x["strain_id"]
        if(StrainAll.objects.filter(strain_id=strain_id)):
            StrainAll.objects.filter(strain_id=strain_id).update(
            bee_host_species = x["bee_host_species"],
            exact_site = x["exact_site"],
            bee_host_id= x["bee_host_id"],
            gut_id = x["gut_id"],
            )
        else:
            StrainAll.objects.create(
            strain_id = x["strain_id"],
            bee_host_species = x["bee_host_species"],
            exact_site = x["exact_site"],
            bee_host_id= x["bee_host_id"],
            gut_id = x["gut_id"],
            )

    taxonomy_origin_data = Taxonomy.objects.all()
    for x in taxonomy_origin_data.values():
        strain_id = x["strain_id"]
        if(StrainAll.objects.filter(strain_id=strain_id)):
            StrainAll.objects.filter(strain_id=strain_id).update(
            strain_phylum =x["strain_phylum"],
            strain_class =x["strain_class"],
            strain_order =x["strain_order"],
            strain_family =x["strain_family"],
            strain_genus =x["strain_genus"],
            strain_species =x["strain_species"],
            )
        else:
            StrainAll.objects.create(
            strain_id =x["strain_id"],
            strain_phylum =x["strain_phylum"],
            strain_class =x["strain_class"],
            strain_order =x["strain_order"],
            strain_family =x["strain_family"],
            strain_genus =x["strain_genus"],
            strain_species =x["strain_species"],
            )


    return redirect('strain_home')