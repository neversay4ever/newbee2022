from django.shortcuts import render,redirect
from django.core import serializers

from .models import BeeAll


def bee_home(request):
    sample_demo = BeeAll.objects.values()[0]
    bee_all = BeeAll.objects.all()

    bee_taxonomy = ['sample_phylum','sample_class','sample_order','sample_family',
                        'sample_genus','sample_species','sample_subspecies','sample_breed']
    taxonomy_data = bee_all.values_list(*bee_taxonomy).distinct() 
        # *bee_taxonomy是将list展开作为参数。 
        # distinct()是去掉重复。
        # values_list的结果形式是[(., ., .),(., ., .)]，方便直接取

    data_taxonomy = []
    for t in taxonomy_data:
        phylum_data = t[0] or ''
        class_data = t[1] or ''
        order_data = t[2] or ''
        family_data = t[3] or ''
        genus_data = t[4] or ''
        species_data = t[5] or ''
        subspecies_data = t[6] or ''
        breed_data = t[7] or ''

        phylum_count = bee_all.filter(sample_phylum=phylum_data).count()
        class_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).count()
        order_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).filter(
                                        sample_order=order_data   
                                        ).count()  
        family_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).filter(
                                        sample_order=order_data   
                                        ).filter(
                                        sample_family=family_data    
                                        ).count() 
        genus_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).filter(
                                        sample_order=order_data   
                                        ).filter(
                                        sample_family=family_data    
                                        ).filter(
                                        sample_genus=genus_data    
                                        ).count()
        species_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).filter(
                                        sample_order=order_data   
                                        ).filter(
                                        sample_family=family_data    
                                        ).filter(
                                        sample_genus=genus_data    
                                        ).filter(
                                        sample_species=species_data    
                                        ).count() 
        subspecies_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).filter(
                                        sample_order=order_data   
                                        ).filter(
                                        sample_family=family_data    
                                        ).filter(
                                        sample_genus=genus_data    
                                        ).filter(
                                        sample_species=species_data    
                                        ).filter(
                                        sample_subspecies=subspecies_data    
                                        ).count()
        breed_count = bee_all.filter(
                                        sample_phylum=phylum_data
                                        ).filter(
                                        sample_class=class_data
                                        ).filter(
                                        sample_order=order_data   
                                        ).filter(
                                        sample_family=family_data    
                                        ).filter(
                                        sample_genus=genus_data    
                                        ).filter(
                                        sample_species=species_data    
                                        ).filter(
                                        sample_subspecies=subspecies_data    
                                        ).filter(
                                        sample_breed=breed_data    
                                        ).count()
        phylum_ids = f'{phylum_data}:null:null:null:null:null'
        class_ids = f'{phylum_data}:{class_data}:null:null:null:null:null:null'
        order_ids = f'{phylum_data}:{class_data}:{order_data}:null:null:null:null:null'
        family_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:null:null:null:null'
        genus_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:null:null:null'
        species_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:null:null'
        subspecies_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:null'
        breed_ids = f'{phylum_data}:{class_data}:{order_data}:{family_data}:{genus_data}:{species_data}:{subspecies_data}:{breed_data}'
            
        data_taxonomy.append({"id": phylum_ids,"parent": "#", "text": phylum_data + " "+ str(phylum_count)})
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

from .models import CollectionData, Taxonomy, SpecimenDetails, HeadthoraxStorage,AbdomenStorage,GutStorage,LegStorage,BeeAll
def bee_data_combine(request):
    collection_data = CollectionData.objects.all()
    for x in collection_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            BeeAll.objects.filter(sample_id=sample_id).update(
            continent_ocean=x["continent_ocean"],
            country=x["country"],
            state_province =x["state_province"],
            city =x["city"],
            county =x["county"],
            town =x["town"],
            village =x["village"],
            exact_site =x["exact_site"],
            latitude =x["latitude"],
            longitude =x["longitude"],
            altitude =x["altitude"],
            geo_notes =x["geo_notes"],
            collector_name =x["collector_name"],
            collection_date =x["collection_date"],
            )
        else:
            BeeAll.objects.create(
            sample_id=x["sample_id"],
            continent_ocean=x["continent_ocean"],
            country=x["country"],
            state_province =x["state_province"],
            city =x["city"],
            county =x["county"],
            town =x["town"],
            village =x["village"],
            exact_site =x["exact_site"],
            latitude =x["latitude"],
            longitude =x["longitude"],
            altitude =x["altitude"],
            geo_notes =x["geo_notes"],
            collector_name =x["collector_name"],
            collection_date =x["collection_date"],
            )

    taxonomy_data = Taxonomy.objects.all()
    for x in taxonomy_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            print('have')
            BeeAll.objects.filter(sample_id=sample_id).update(
            sample_phylum = x["sample_phylum"],
            sample_class = x["sample_class"],
            sample_order = x["sample_order"],
            sample_family = x["sample_family"],
            sample_genus = x["sample_genus"],
            sample_species = x["sample_species"],
            sample_subspecies = x["sample_subspecies"],
            sample_breed = x["sample_breed"],
            identifier_name = x["identifier_name"],
            identifier_email = x["identifier_email"],
            identifier_institution = x["identifier_institution"],
            barcode_result = x["barcode_result"],
            )
        else:
            print(x)
            BeeAll.objects.create(
            sample_id=x["sample_id"],
            sample_phylum = x["sample_phylum"],
            sample_class = x["sample_class"],
            sample_order = x["sample_order"],
            sample_family = x["sample_family"],
            sample_genus = x["sample_genus"],
            sample_species = x["sample_species"],
            sample_subspecies = x["sample_subspecies"],
            sample_breed = x["sample_breed"],
            identifier_name = x["identifier_name"],
            identifier_email = x["identifier_email"],
            identifier_institution = x["identifier_institution"],
            barcode_result = x["barcode_result"],
            )

    specimen_details_data = SpecimenDetails.objects.all()
    for x in specimen_details_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            BeeAll.objects.filter(sample_id=sample_id).update(
            multi_num =x["multi_num"],
            caste_type =x["caste_type"],
            labor_division =x["labor_division"],
            life_style =x["life_style"],
            beekeeper =x["beekeeper"],
            apiary_id =x["apiary_id"],
            hive_id =x["hive_id"],
            host_origin =x["host_origin"],
            hive_year =x["hive_year"],
            decapping_freq =x["decapping_freq"],
            feeding_or_not =x["feeding_or_not"],
            feeding_description =x["feeding_description"],
            habitat_type =x["habitat_type"],
            habitat_photo_file_path =x["habitat_photo_file_path"],
            pesticide_or_not =x["pesticide_or_not"],
            pesticide_detail =x["pesticide_detail"],
            flower_species =x["flower_species"],
            flower_photo_file_path =x["flower_photo_file_path"],
            record_by_who =x["record_by_who"],
            record_datetime =x["record_datetime"],
            sample_notes =x["sample_notes"],
            )
        else:
            BeeAll.objects.create(
            sample_id =x["sample_id"],
            multi_num =x["multi_num"],
            caste_type =x["caste_type"],
            labor_division =x["labor_division"],
            life_style =x["life_style"],
            beekeeper =x["beekeeper"],
            apiary_id =x["apiary_id"],
            hive_id =x["hive_id"],
            host_origin =x["host_origin"],
            hive_year =x["hive_year"],
            decapping_freq =x["decapping_freq"],
            feeding_or_not =x["feeding_or_not"],
            feeding_description =x["feeding_description"],
            habitat_type =x["habitat_type"],
            habitat_photo_file_path =x["habitat_photo_file_path"],
            pesticide_or_not =x["pesticide_or_not"],
            pesticide_detail =x["pesticide_detail"],
            flower_species =x["flower_species"],
            flower_photo_file_path =x["flower_photo_file_path"],
            record_by_who =x["record_by_who"],
            record_datetime =x["record_datetime"],
            sample_notes =x["sample_notes"],
        )
    
    headthorax_storage_data = HeadthoraxStorage.objects.all()
    for x in headthorax_storage_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            BeeAll.objects.filter(sample_id=sample_id).update(
            headthorax_id =x["headthorax_id"],
            headthorax_preservation =x["headthorax_preservation"],
            headthorax_usage =x["headthorax_usage"],
            thorax_dessection =x["thorax_dessection"],
            headthorax_box_id =x["headthorax_box_id"],
            headthorax_storage_location =x["headthorax_storage_location"],
            )
        else:
            BeeAll.objects.create(
            sample_id =x["sample_id"],
            headthorax_id =x["headthorax_id"],
            headthorax_preservation =x["headthorax_preservation"],
            headthorax_usage =x["headthorax_usage"],
            thorax_dessection =x["thorax_dessection"],
            headthorax_box_id =x["headthorax_box_id"],
            headthorax_storage_location =x["headthorax_storage_location"],
        )
    
    abdomen_storage_data = AbdomenStorage.objects.all()
    for x in abdomen_storage_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            BeeAll.objects.filter(sample_id=sample_id).update(
            abdomen_id =x["abdomen_id"],
            abdomen_preservation =x["abdomen_preservation"],
            abdomen_usage =x["abdomen_usage"],
            abdomen_dissection_state =x["abdomen_dissection_state"],
            abdomen_box_id =x["abdomen_box_id"],
            abdomen_storage_location =x["abdomen_storage_location"],
            )
        else:
            BeeAll.objects.create(
            sample_id =x["sample_id"],
            abdomen_id =x["abdomen_id"],
            abdomen_preservation =x["abdomen_preservation"],
            abdomen_usage =x["abdomen_usage"],
            abdomen_dissection_state =x["abdomen_dissection_state"],
            abdomen_box_id =x["abdomen_box_id"],
            abdomen_storage_location =x["abdomen_storage_location"],
        )

    gut_storage_data = GutStorage.objects.all()
    for x in gut_storage_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            BeeAll.objects.filter(sample_id=sample_id).update(
            gut_id =x["gut_id"],
            gut_storage =x["gut_storage"],
            gut_usage =x["gut_usage"],
            gut_dissection_state =x["gut_dissection_state"],
            gut_box_id =x["gut_box_id"],
            gut_storage_location =x["gut_storage_location"],
            )
        else:
            BeeAll.objects.create(
            sample_id  = x.sample_id ,
            gut_id =x["gut_id"],
            gut_storage =x["gut_storage"],
            gut_usage =x["gut_usage"],
            gut_dissection_state =x["gut_dissection_state"],
            gut_box_id =x["gut_box_id"],
            gut_storage_location =x["gut_storage_location"],
        )
    
    leg_storage_data = LegStorage.objects.all()
    for x in leg_storage_data.values():
        sample_id = x["sample_id"]
        if(BeeAll.objects.filter(sample_id=sample_id)):
            BeeAll.objects.filter(sample_id=sample_id).update(
            leg_id =x["leg_id"],
            leg_storage =x["leg_storage"],
            leg_usage =x["leg_usage"],
            leg_dissection_state =x["leg_dissection_state"],
            leg_box_id =x["leg_box_id"],
            )
        else:
            BeeAll.objects.create(
            sample_id =x["sample_id"],
            leg_id =x["leg_id"],
            leg_storage =x["leg_storage"],
            leg_usage =x["leg_usage"],
            leg_dissection_state =x["leg_dissection_state"],
            leg_box_id =x["leg_box_id"],
        )
    return redirect('bee_home')


