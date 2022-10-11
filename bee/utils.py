
def getBeeTaxonomyData4jstree(SampleModel):
        # sample_phylum = models.CharField(_("门"), max_length=50,null=True, blank=True)
        # sample_class = models.CharField(_("纲"), max_length=50,null=True, blank=True)
        # sample_order = models.CharField(_("目"), max_length=50,null=True, blank=True)
        # sample_family = models.CharField(_("科"), max_length=50,null=True, blank=True)
        # sample_genus = models.CharField(_("属"), max_length=50,null=True, blank=True)
        # sample_species = models.CharField(_("种"), max_length=50,null=True, blank=True)
        # sample_subspecies = models.CharField(_("亚种"), max_length=50,null=True, blank=True)
        # sample_breed = models.CharField(_("品种"), max_length=50,null=True, blank=True)

    bee_all = SampleModel.objects.all()
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
    return(data)