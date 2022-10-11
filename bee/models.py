from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CollectionData(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50, null=True, blank=True)
    continent_ocean = models.CharField(_("大洲"), max_length=50, null=True, blank=True)
    country = models.CharField(_("国家"), max_length=50, null=True, blank=True)
    state_province = models.CharField(_("省"), max_length=50, null=True, blank=True)
    city = models.CharField(_("市"), max_length=50, null=True, blank=True)
    county = models.CharField(_("县"), max_length=50, null=True, blank=True)
    town = models.CharField(_("乡镇"), max_length=50, null=True, blank=True)
    village = models.CharField(_("村"), max_length=50, null=True, blank=True)
    exact_site = models.CharField(_("采集地简要信息"), max_length=250, null=True, blank=True)
    latitude = models.FloatField(_("纬度"),null=True, blank=True)
    longitude = models.FloatField(_("经度"),null=True, blank=True)
    altitude = models.IntegerField(_("海拔"),null=True, blank=True)
    geo_notes = models.TextField(_("采集地备注"),null=True, blank=True)
    collector_name = models.CharField(_("采集人"), max_length=50,null=True, blank=True)
    collection_date = models.DateField(_("采集日期"), auto_now=False, auto_now_add=False,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_采集信息'
        verbose_name_plural = '蜜蜂_采集信息'

    def __str__(self):
        return f'{self.sample_id}-{self.exact_site}'

class Taxonomy(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50,null=True, blank=True)
    sample_phylum = models.CharField(_("门"), max_length=50,null=True, blank=True)
    sample_class = models.CharField(_("纲"), max_length=50,null=True, blank=True)
    sample_order = models.CharField(_("目"), max_length=50,null=True, blank=True)
    sample_family = models.CharField(_("科"), max_length=50,null=True, blank=True)
    sample_genus = models.CharField(_("属"), max_length=50,null=True, blank=True)
    sample_species = models.CharField(_("种"), max_length=50,null=True, blank=True)
    sample_subspecies = models.CharField(_("亚种"), max_length=50,null=True, blank=True)
    sample_breed = models.CharField(_("品种"), max_length=50,null=True, blank=True)
    identifier_name = models.CharField(_("鉴定人"), max_length=50,null=True, blank=True)
    identifier_email = models.EmailField(_("鉴定人邮箱"), max_length=254,null=True, blank=True)
    identifier_institution = models.CharField(_("鉴定人单位"), max_length=250,null=True, blank=True)
    barcode_result = models.CharField(_("是否有条形码"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_分类信息'
        verbose_name_plural = '蜜蜂_分类信息'
    def __str__(self):
        return f'{self.sample_id}-{self.sample_species}'

class SpecimenDetails(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50,null=True, blank=True)
    multi_num = models.IntegerField(_("同管个体数目"),default=1)
    caste_type = models.CharField(_("级型"), max_length=50,null=True, blank=True)
    labor_division = models.CharField(_("分工"), max_length=50,null=True, blank=True)
    life_style = models.CharField(_("饲养方式"), max_length=50,null=True, blank=True)
    life_stage = models.CharField(_("生活史"), max_length=50,null=True, blank=True)
    beekeeper = models.CharField(_("养蜂人"), max_length=50,null=True, blank=True)
    apiary_id = models.CharField(_("蜂场编号"), max_length=50,null=True, blank=True)
    hive_id = models.CharField(_("蜂箱编号"), max_length=50,null=True, blank=True)
    host_origin = models.CharField(_("蜂群来源"), max_length=50,null=True, blank=True)
    hive_year = models.CharField(_("蜂群保有年限"), max_length=50,null=True, blank=True)
    decapping_freq = models.CharField(_("年取蜜频次"), max_length=50,null=True, blank=True)
    feeding_or_not = models.CharField(_("是否喂食花粉蔗糖"), max_length=50,null=True, blank=True)
    feeding_description = models.CharField(_("喂食细节"), max_length=250,null=True, blank=True)
    habitat_type = models.CharField(_("生境类型"), max_length=50,null=True, blank=True)
    habitat_photo_file_path = models.CharField(_("生境照片存储位置"), max_length=250,null=True, blank=True)
    pesticide_or_not = models.CharField(_("是否用药"), max_length=50,null=True, blank=True)
    pesticide_detail = models.CharField(_("用药细节"), max_length=250,null=True, blank=True)
    flower_species = models.CharField(_("蜜粉源植物"), max_length=250,null=True, blank=True)
    flower_photo_file_path = models.CharField(_("蜜粉源植物照片存储位置"), max_length=250,null=True, blank=True)
    record_by_who = models.CharField(_("记录人"), max_length=50,null=True, blank=True)
    record_datetime = models.DateField(_("记录日期"), auto_now=False, auto_now_add=False,null=True, blank=True)
    sample_notes = models.TextField(_("样本备注"),null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_标本信息'
        verbose_name_plural = '蜜蜂_标本信息'

    def __str__(self):
        return f'{self.sample_id}-{self.beekeeper}-{self.record_by_who}'

class HeadthoraxStorage(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50,null=True, blank=True)
    headthorax_id = models.CharField(_("头胸组织编号"), max_length=50,null=True, blank=True)
    headthorax_preservation = models.CharField(_("头胸组织保存方法"), max_length=50,null=True, blank=True)
    headthorax_usage = models.CharField(_("头胸用途"), max_length=50,null=True, blank=True)
    thorax_dessection = models.CharField(_("解剖状态"), max_length=50,null=True, blank=True)
    headthorax_box_id = models.CharField(_("头胸组织盒编号"), max_length=50,null=True, blank=True)
    headthorax_storage_location = models.CharField(_("头胸组织存储位置"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_头胸组织存储'
        verbose_name_plural = '蜜蜂_头胸组织存储'

    def __str__(self):
        return f'{self.sample_id}-{self.headthorax_id}-{self.headthorax_storage_location}'


class AbdomenStorage(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50,null=True, blank=True)
    abdomen_id = models.CharField(_("腹部组织编号"), max_length=50,null=True, blank=True)
    abdomen_preservation = models.CharField(_("腹部组织保存方法"), max_length=50,null=True, blank=True)
    abdomen_usage = models.CharField(_("腹部用途"), max_length=50,null=True, blank=True)
    abdomen_dissection_state = models.CharField(_("腹部解剖状态"), max_length=50,null=True, blank=True)
    abdomen_box_id = models.CharField(_("腹部组织样本盒编号"), max_length=50,null=True, blank=True)
    abdomen_storage_location = models.CharField(_("腹部组织保存位置"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_腹部组织存储'
        verbose_name_plural = '蜜蜂_腹部组织存储'

    def __str__(self):
        return f'{self.sample_id}-{self.abdomen_id}-{self.abdomen_storage_location}'


class GutStorage(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50,null=True, blank=True)
    gut_id = models.CharField(_("肠道组织编号"), max_length=50,null=True, blank=True)
    gut_storage = models.CharField(_("肠道组织保存方法"), max_length=50,null=True, blank=True)
    gut_usage = models.CharField(_("肠道用途"), max_length=50,null=True, blank=True)
    gut_dissection_state = models.CharField(_("肠道解剖状态"), max_length=50,null=True, blank=True)
    gut_box_id = models.CharField(_("肠道组织样本盒编号"), max_length=50,null=True, blank=True)
    gut_storage_location = models.CharField(_("肠道组织保存位置"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_肠道组织存储'
        verbose_name_plural = '蜜蜂_肠道组织存储'

    def __str__(self):
        return f'{self.sample_id}-{self.gut_id}-{self.gut_storage_location}'



class LegStorage(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50,null=True, blank=True)
    leg_id = models.CharField(_("足组织编号"), max_length=50,null=True, blank=True)
    leg_storage = models.CharField(_("足组织保存方法"), max_length=50,null=True, blank=True)
    leg_usage = models.CharField(_("足用途"), max_length=50,null=True, blank=True)
    leg_dissection_state = models.CharField(_("足解剖状态"), max_length=50,null=True, blank=True)
    leg_box_id = models.CharField(_("足组织样本盒编号"), max_length=50,null=True, blank=True)
    leg_storage_location = models.CharField(_("足组织保存位置"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_足组织存储'
        verbose_name_plural = '蜜蜂_足组织存储'
    
    def __str__(self):
        return f'{self.sample_id}-{self.leg_id}-{self.leg_storage_location}'



class BeeAll(models.Model):
    sample_id = models.CharField(_("标本编号"), max_length=50, null=True, blank=True)
    continent_ocean = models.CharField(_("大洲"), max_length=50, null=True, blank=True)
    country = models.CharField(_("国家"), max_length=50, null=True, blank=True)
    state_province = models.CharField(_("省"), max_length=50, null=True, blank=True)
    city = models.CharField(_("市"), max_length=50, null=True, blank=True)
    county = models.CharField(_("县"), max_length=50, null=True, blank=True)
    town = models.CharField(_("乡镇"), max_length=50, null=True, blank=True)
    village = models.CharField(_("村"), max_length=50, null=True, blank=True)
    exact_site = models.CharField(_("采集地简要信息"), max_length=250, null=True, blank=True)
    latitude = models.FloatField(_("纬度"),null=True, blank=True)
    longitude = models.FloatField(_("经度"),null=True, blank=True)
    altitude = models.IntegerField(_("海拔"),null=True, blank=True)
    geo_notes = models.TextField(_("采集地备注"),null=True, blank=True)
    collector_name = models.CharField(_("采集人"), max_length=50,null=True, blank=True)
    collection_date = models.DateField(_("采集日期"), auto_now=False, auto_now_add=False,null=True, blank=True)

    sample_phylum = models.CharField(_("门"), max_length=50,null=True, blank=True)
    sample_class = models.CharField(_("纲"), max_length=50,null=True, blank=True)
    sample_order = models.CharField(_("目"), max_length=50,null=True, blank=True)
    sample_family = models.CharField(_("科"), max_length=50,null=True, blank=True)
    sample_genus = models.CharField(_("属"), max_length=50,null=True, blank=True)
    sample_species = models.CharField(_("种"), max_length=50,null=True, blank=True)
    sample_subspecies = models.CharField(_("亚种"), max_length=50,null=True, blank=True)
    sample_breed = models.CharField(_("品种"), max_length=50,null=True, blank=True)
    identifier_name = models.CharField(_("鉴定人"), max_length=50,null=True, blank=True)
    identifier_email = models.EmailField(_("鉴定人邮箱"), max_length=254,null=True, blank=True)
    identifier_institution = models.CharField(_("鉴定人单位"), max_length=250,null=True, blank=True)
    barcode_result = models.CharField(_("是否有条形码"), max_length=50,null=True, blank=True)

    multi_num = models.IntegerField(_("同管个体数目"),default=1)
    caste_type = models.CharField(_("级型"), max_length=50,null=True, blank=True)
    labor_division = models.CharField(_("分工"), max_length=50,null=True, blank=True)
    life_style = models.CharField(_("饲养方式"), max_length=50,null=True, blank=True)
    life_stage = models.CharField(_("生活史"), max_length=50,null=True, blank=True)
    beekeeper = models.CharField(_("养蜂人"), max_length=50,null=True, blank=True)
    apiary_id = models.CharField(_("蜂场编号"), max_length=50,null=True, blank=True)
    hive_id = models.CharField(_("蜂箱编号"), max_length=50,null=True, blank=True)
    host_origin = models.CharField(_("蜂群来源"), max_length=50,null=True, blank=True)
    hive_year = models.CharField(_("蜂群保有年限"), max_length=50,null=True, blank=True)
    decapping_freq = models.CharField(_("年取蜜频次"), max_length=50,null=True, blank=True)
    feeding_or_not = models.CharField(_("是否喂食花粉蔗糖"), max_length=50,null=True, blank=True)
    feeding_description = models.CharField(_("喂食细节"), max_length=250,null=True, blank=True)
    habitat_type = models.CharField(_("生境类型"), max_length=50,null=True, blank=True)
    habitat_photo_file_path = models.CharField(_("生境照片存储位置"), max_length=250,null=True, blank=True)
    pesticide_or_not = models.CharField(_("是否用药"), max_length=50,null=True, blank=True)
    pesticide_detail = models.CharField(_("用药细节"), max_length=250,null=True, blank=True)
    flower_species = models.CharField(_("蜜粉源植物"), max_length=250,null=True, blank=True)
    flower_photo_file_path = models.CharField(_("蜜粉源植物照片存储位置"), max_length=250,null=True, blank=True)
    record_by_who = models.CharField(_("记录人"), max_length=50,null=True, blank=True)
    record_datetime = models.DateField(_("记录日期"), auto_now=False, auto_now_add=False,null=True, blank=True)
    sample_notes = models.TextField(_("样本备注"),null=True, blank=True)

    headthorax_id = models.CharField(_("头胸组织编号"), max_length=50,null=True, blank=True)
    headthorax_preservation = models.CharField(_("头胸组织保存方法"), max_length=50,null=True, blank=True)
    headthorax_usage = models.CharField(_("头胸用途"), max_length=50,null=True, blank=True)
    thorax_dessection = models.CharField(_("解剖状态"), max_length=50,null=True, blank=True)
    headthorax_box_id = models.CharField(_("头胸组织盒编号"), max_length=50,null=True, blank=True)
    headthorax_storage_location = models.CharField(_("头胸组织存储位置"), max_length=50,null=True, blank=True)

    abdomen_id = models.CharField(_("腹部组织编号"), max_length=50,null=True, blank=True)
    abdomen_preservation = models.CharField(_("腹部组织保存方法"), max_length=50,null=True, blank=True)
    abdomen_usage = models.CharField(_("腹部用途"), max_length=50,null=True, blank=True)
    abdomen_dissection_state = models.CharField(_("腹部解剖状态"), max_length=50,null=True, blank=True)
    abdomen_box_id = models.CharField(_("腹部组织样本盒编号"), max_length=50,null=True, blank=True)
    abdomen_storage_location = models.CharField(_("腹部组织保存位置"), max_length=50,null=True, blank=True)

    gut_id = models.CharField(_("肠道组织编号"), max_length=50,null=True, blank=True)
    gut_storage = models.CharField(_("肠道组织保存方法"), max_length=50,null=True, blank=True)
    gut_usage = models.CharField(_("肠道用途"), max_length=50,null=True, blank=True)
    gut_dissection_state = models.CharField(_("肠道解剖状态"), max_length=50,null=True, blank=True)
    gut_box_id = models.CharField(_("肠道组织样本盒编号"), max_length=50,null=True, blank=True)
    gut_storage_location = models.CharField(_("肠道组织保存位置"), max_length=50,null=True, blank=True)

    leg_id = models.CharField(_("足组织编号"), max_length=50,null=True, blank=True)
    leg_storage = models.CharField(_("足组织保存方法"), max_length=50,null=True, blank=True)
    leg_usage = models.CharField(_("足用途"), max_length=50,null=True, blank=True)
    leg_dissection_state = models.CharField(_("足解剖状态"), max_length=50,null=True, blank=True)
    leg_box_id = models.CharField(_("足组织样本盒编号"), max_length=50,null=True, blank=True)
    leg_storage_location = models.CharField(_("足组织保存位置"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜜蜂_总表'
        verbose_name_plural = '蜜蜂_总表'

    def __str__(self):
        return f'{self.sample_id}-{self.exact_site}-{self.life_style}'

