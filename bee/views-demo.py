from django.shortcuts import render
# Create your views here.

from .models import BeeAll, Taxonomy

from .filters import BeeAllFilter
from django.shortcuts import render
from django.db.models import Count

from django.views.decorators.cache import cache_page

sample_list = BeeAll.objects.all()
gut_storage_count = sample_list.values('gut_storage').annotate(count=Count('gut_storage')).distinct()
gut_usage_count = sample_list.values('gut_usage').annotate(count=Count('gut_usage')).distinct()
headthorax_preservation_count = sample_list.values('headthorax_preservation').annotate(count=Count('headthorax_preservation')).distinct()
headchest_usage_count = sample_list.values('headchest_usage').annotate(count=Count('headchest_usage')).distinct()
leg_storage_count = sample_list.values('leg_storage').annotate(count=Count('leg_storage')).distinct()
leg_usage_count = sample_list.values('leg_usage').annotate(count=Count('leg_usage')).distinct()
abdomen_preservation_count = sample_list.values('abdomen_preservation').annotate(count=Count('abdomen_preservation')).distinct()
abdomen_usage_count = sample_list.values('abdomen_usage').annotate(count=Count('abdomen_usage')).distinct()

gut_storage_array = [f'{m.get("gut_storage")}:{m.get("count")}' for m in gut_storage_count]
gut_usage_array = [f'{m.get("gut_usage")}:{m.get("count")}' for m in gut_usage_count]
headthorax_preservation_array = [f'{m.get("headthorax_preservation")}:{m.get("count")}' for m in headthorax_preservation_count]
headchest_usage_array = [f'{m.get("headchest_usage")}:{m.get("count")}' for m in headchest_usage_count]
leg_storage_array = [f'{m.get("leg_storage")}:{m.get("count")}' for m in leg_storage_count]
leg_usage_array = [f'{m.get("leg_usage")}:{m.get("count")}' for m in leg_usage_count]
abdomen_preservation_array = [f'{m.get("abdomen_preservation")}:{m.get("count")}' for m in abdomen_preservation_count]
abdomen_usage_array = [f'{m.get("abdomen_usage")}:{m.get("count")}' for m in abdomen_usage_count]

@cache_page(60 * 15)
def search(request):
    sample_filter = BeeAllFilter(request.GET,queryset=BeeAll.objects.select_related().all())
    print(sample_filter)

    bee_taxonomy = Taxonomy.objects.values()
    bee_sample_query = sample_filter.qs
    data_taxonomy = []

    print(sample_filter.qs)
    for t in bee_taxonomy:
        phylum_data = t.get('bee_phylum') 
        class_data = t.get('bee_class') 
        order_data = t.get('bee_order') 
        family_data = t.get('bee_family') 
        genus_data = t.get('bee_genus')
        species_data = t.get('bee_species') 
        subspecies_data = t.get('bee_subspecies')
        breed_data = t.get('bee_breed')

        phylum_count = bee_sample_query.filter(bee_taxonomy__bee_phylum=phylum_data).count()
        class_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).count()
        order_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).filter(
                                        bee_taxonomy__bee_order=order_data   
                                        ).count()  
        family_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).filter(
                                        bee_taxonomy__bee_order=order_data   
                                        ).filter(
                                        bee_taxonomy__bee_family=family_data    
                                        ).count() 
        genus_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).filter(
                                        bee_taxonomy__bee_order=order_data   
                                        ).filter(
                                        bee_taxonomy__bee_family=family_data    
                                        ).filter(
                                        bee_taxonomy__bee_genus=genus_data    
                                        ).count()
        species_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).filter(
                                        bee_taxonomy__bee_order=order_data   
                                        ).filter(
                                        bee_taxonomy__bee_family=family_data    
                                        ).filter(
                                        bee_taxonomy__bee_genus=genus_data    
                                        ).filter(
                                        bee_taxonomy__bee_species=species_data    
                                        ).count() 
        subspecies_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).filter(
                                        bee_taxonomy__bee_order=order_data   
                                        ).filter(
                                        bee_taxonomy__bee_family=family_data    
                                        ).filter(
                                        bee_taxonomy__bee_genus=genus_data    
                                        ).filter(
                                        bee_taxonomy__bee_species=species_data    
                                        ).filter(
                                        bee_taxonomy__bee_subspecies=subspecies_data    
                                        ).count()
        breed_count = bee_sample_query.filter(
                                        bee_taxonomy__bee_phylum=phylum_data
                                        ).filter(
                                        bee_taxonomy__bee_class=class_data
                                        ).filter(
                                        bee_taxonomy__bee_order=order_data   
                                        ).filter(
                                        bee_taxonomy__bee_family=family_data    
                                        ).filter(
                                        bee_taxonomy__bee_genus=genus_data    
                                        ).filter(
                                        bee_taxonomy__bee_species=species_data    
                                        ).filter(
                                        bee_taxonomy__bee_subspecies=subspecies_data    
                                        ).filter(
                                        bee_taxonomy__bee_breed=breed_data    
                                        ).count()
        phylum_ids = f'{phylum_data}:null:null:null:null:null'
        class_ids = f'{phylum_data}:{class_data}:null:null:null:null:null:null'
        order_ids = f'{phylum_data}:{class_data}:{order_data}:null:null:null:null:null'
        family_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:null:null:null:null'
        genus_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:null:null:null'
        species_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:null:null'
        subspecies_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:null'
        breed_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:{breed_data}'
            
        data_taxonomy.append({"id": phylum_ids,"parent": "#", "text": phylum_data +" "+ str(phylum_count)})
        data_taxonomy.append({"id": class_ids,"parent": phylum_ids, "text": class_data+" "+ str(class_count)})
        data_taxonomy.append({"id": order_ids,"parent": class_ids, "text": order_data+" "+ str(order_count)})
        data_taxonomy.append({"id": family_ids,"parent": order_ids, "text": family_data+" "+ str(family_count)})
        if genus_data == 'Apis':
            data_taxonomy.append({"id": genus_ids,"parent": family_ids,  "text":genus_data+" "+ str(genus_count), "state" : {"selected": "true" },})
        else:
            data_taxonomy.append({"id": genus_ids,"parent": family_ids,  "text":genus_data+" "+ str(genus_count),})
        data_taxonomy.append({"id": species_ids,"parent": genus_ids, "text": species_data+" "+ str(species_count)})
        data_taxonomy.append({"id": subspecies_ids,"parent": species_ids, "text": subspecies_data+" "+ str(subspecies_count)})
        data_taxonomy.append({"id": breed_ids,"parent": subspecies_ids, "text": breed_data+" "+ str(breed_count)})


    res = []
    for i in data_taxonomy:
        if i not in res:
            res.append(i)

    data = f'data_taxonomy={res}'
    
    sample_demo = BeeAll.objects.values()[0]
    print(sample_demo)
    return render(request, 'bee/bee_home.html', {'filter': sample_filter, 'data': data, 'sample_demo': sample_demo})

from django.core import serializers
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

@cache_page(60 * 15)
def getData(request, data_string):
    # Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:北方中蜂-Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:海南中蜂
    selected_sample = BeeAll.objects.none()
    if not data_string:
        selected_sample = BeeAll.objects.all()
    data_string = data_string.strip("'")
    data_array = data_string.split('-')
    selected_sample = BeeAll.objects.none()
    
    for data in data_array:
        data_taxonomy_array = data.split(':')
        filter_q = {}
        if data_taxonomy_array[0] and data_taxonomy_array[0] != "null":
            filter_q['bee_taxonomy__bee_phylum__startswith']=data_taxonomy_array[0]

        if data_taxonomy_array[1] and data_taxonomy_array[1] != "null":
            filter_q ['bee_taxonomy__bee_class__startswith']=data_taxonomy_array[1]

        if data_taxonomy_array[2] and data_taxonomy_array[2] != "null":
            filter_q['bee_taxonomy__bee_order__startswith'] =data_taxonomy_array[2]

        if len(data_taxonomy_array)>=4 and data_taxonomy_array[3] != "null":
            filter_q['bee_taxonomy__bee_family__startswith']=data_taxonomy_array[3]

        if len(data_taxonomy_array)>=5 and data_taxonomy_array[4] != "null":
            filter_q['bee_taxonomy__bee_genus__startswith']=data_taxonomy_array[4]

        if len(data_taxonomy_array)>=6 and data_taxonomy_array[5] != "null":
            filter_q['bee_taxonomy__bee_species__startswith']=data_taxonomy_array[5]

        if len(data_taxonomy_array)>=7 and data_taxonomy_array[6] != "null":
            filter_q['bee_taxonomy__bee_subspecies__startswith']=data_taxonomy_array[6]

        if len(data_taxonomy_array)>=8 and data_taxonomy_array[7] != "null":
            filter_q['bee_taxonomy__bee_breed__startswith']=data_taxonomy_array[7]

        sample_queryset = BeeAll.objects.filter(**filter_q)
        selected_sample = selected_sample | sample_queryset

    # stat gut_storage, gut_usage etc. for chart
    stat_gut_storage = selected_sample.values('gut_storage').annotate(count=Count('gut_storage')).distinct()
    stat_gut_usage = selected_sample.values('gut_usage').annotate(count=Count('gut_usage')).distinct()
    stat_headthorax_preservation = selected_sample.values('headthorax_preservation').annotate(count=Count('headthorax_preservation')).distinct()
    stat_headchest_usage = selected_sample.values('headchest_usage').annotate(count=Count('headchest_usage')).distinct()
    stat_abdomen_preservation = selected_sample.values('abdomen_preservation').annotate(count=Count('abdomen_preservation')).distinct()
    stat_abdomen_usage = selected_sample.values('abdomen_usage').annotate(count=Count('abdomen_usage')).distinct()
    stat_leg_storage = selected_sample.values('leg_storage').annotate(count=Count('leg_storage')).distinct()
    stat_leg_usage = selected_sample.values('leg_usage').annotate(count=Count('leg_usage')).distinct()
    stat_location = selected_sample.select_related().values('bee_location__exact_site','bee_location__longitude','bee_location__latitude').annotate(count=Count('bee_location')).distinct()

    if selected_sample == BeeAll.objects.none():
        selected_sample = BeeAll.objects.all()

    obj = {
        'stat_gut_storage': json.dumps(list(stat_gut_storage)),  # 可以不加 cls=DjangoJSONEncoder
        'stat_gut_usage': json.dumps(list(stat_gut_usage),cls=DjangoJSONEncoder),  # 核心在于用 list()将queryset变为python数据结构
        'stat_headthorax_preservation': json.dumps(list(stat_headthorax_preservation),cls=DjangoJSONEncoder),
        'stat_headchest_usage': json.dumps(list(stat_headchest_usage),cls=DjangoJSONEncoder),
        'stat_abdomen_preservation': json.dumps(list(stat_abdomen_preservation),cls=DjangoJSONEncoder),
        'stat_abdomen_usage': json.dumps(list(stat_abdomen_usage),cls=DjangoJSONEncoder),
        'stat_leg_storage': json.dumps(list(stat_leg_storage),cls=DjangoJSONEncoder),
        'stat_leg_usage':json.dumps(list(stat_leg_usage),cls=DjangoJSONEncoder),
        'stat_location': json.dumps(list(stat_location),cls=DjangoJSONEncoder),
        'selected_sample':serializers.serialize('json', selected_sample),
    }
    return HttpResponse(json.dumps(obj), content_type='application/json')


            
def each(request):
    pass
