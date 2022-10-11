from django.shortcuts import render
from django.core import serializers

from .utils import getBeeTaxonomyData4jstree
from .models import BeeAll

data = getBeeTaxonomyData4jstree(BeeAll)  # 单独处理数据是为了一次性处理备用，不用每次request都调用数据处理函数
sample_demo = BeeAll.objects.values()[0]
bee_all = BeeAll.objects.all()

def bee_home(request):
    return render(request, 'bee/bee_home.html', {'data': data, 'sample_demo': sample_demo, 'bee_all':serializers.serialize('json', bee_all)})


from django.http import HttpResponse
import json
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def getBeeJsonFromJstree(request, data_string):
    # breed_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:{breed_data}'
    # Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:北方中蜂-Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:海南中蜂
    selected_sample = BeeAll.objects.none()
    if not data_string:
        selected_sample = BeeAll.objects.values('sample_id')
        obj = {
        'selected_sample':serializers.serialize('json', selected_sample),
              }
        return HttpResponse(json.dumps(obj), content_type='application/json')

    data_string = data_string.strip("'")
    print(data_string)
    data_array = data_string.split('-')
    #data_string = data.selected.join('-')    // data selected in jstree 在前端自定义的连接符
    selected_sample = BeeAll.objects.none()
    
    for data in data_array:
        data_taxonomy_array = data.split(':')
        filter_q = {}
        if data_taxonomy_array[0] and data_taxonomy_array[0] != "null":
            filter_q['sample_phylum__startswith']=data_taxonomy_array[0]

        if data_taxonomy_array[1] and data_taxonomy_array[1] != "null":
            filter_q ['sample_class__startswith']=data_taxonomy_array[1]

        if data_taxonomy_array[2] and data_taxonomy_array[2] != "null":
            filter_q['sample_order__startswith'] =data_taxonomy_array[2]

        if len(data_taxonomy_array)>=4 and data_taxonomy_array[3] != "null":
            filter_q['sample_family__startswith']=data_taxonomy_array[3]

        if len(data_taxonomy_array)>=5 and data_taxonomy_array[4] != "null":
            filter_q['sample_genus__startswith']=data_taxonomy_array[4]

        if len(data_taxonomy_array)>=6 and data_taxonomy_array[5] != "null":
            filter_q['sample_species__startswith']=data_taxonomy_array[5]

        if len(data_taxonomy_array)>=7 and data_taxonomy_array[6] != "null":
            filter_q['sample_subspecies__startswith']=data_taxonomy_array[6]

        if len(data_taxonomy_array)>=8 and data_taxonomy_array[7] != "null":
            filter_q['sample_breed__startswith']=data_taxonomy_array[7]

        sample_queryset = BeeAll.objects.filter(**filter_q)
        selected_sample = selected_sample | sample_queryset

    if selected_sample == BeeAll.objects.none():
        selected_sample = BeeAll.objects.values('sample_id')

    obj = {
        'selected_sample_id':serializers.serialize('json', selected_sample),
    }
    return HttpResponse(json.dumps(obj), content_type='application/json')

def bee_single(request, sample_id):
    # breed_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:{breed_data}'
    # Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:北方中蜂-Euarthropoda:Insecta:Hymenoptera:Apidae:Apis:Apis cerana:Apis cerana cerana:海南中蜂
    sample = BeeAll.objects.filter(sample_id=sample_id)
    print(sample)
    return render(request, 'bee/bee_single.html', {'samples': sample})

    