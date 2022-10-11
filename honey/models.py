from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class HoneyCollector(models.Model):
    honey_collector_code = models.CharField(_("采集人编号"), max_length=50,null=True, blank=True)
    honey_collector = models.CharField(_("采集人"), max_length=50,null=True, blank=True)
    collector_phone = models.CharField(_("联系电话"), max_length=50,null=True, blank=True)
    collector_email = models.CharField(_("邮箱"), max_length=50,null=True, blank=True)
    collector_address = models.CharField(_("地址"), max_length=150,null=True, blank=True)
    collector_note = models.TextField(_("采集人备注"),null=True, blank=True)
    
    class Meta:
        verbose_name = '蜂蜜_采集人信息'
        verbose_name_plural = '蜂蜜_采集人信息'

    def __str__(self):
        return f'{self.honey_collector}-{self.collector_phone}'



class HoneyIngredients(models.Model):
    honey_sample_id = models.CharField(_("蜂蜜编号"), max_length=50,null=True, blank=True)
    taxon_species = models.CharField(_("成份物种名"), max_length=50,null=True, blank=True)
    taxon_species_chinese = models.CharField(_("成份物种中文名"), max_length=50,null=True, blank=True)
    abundance_percentage = models.CharField(_("丰度百分比"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜_成份'
        verbose_name_plural = '蜂蜜_成份'

    def __str__(self):
        return f'{self.honey_sample_id}-{self.taxon_species}-{self.taxon_species_chinese}'


class HoneyRefGenome(models.Model):
    taxon_id = models.CharField(_("分类编号"), max_length=50,null=True, blank=True)
    taxon_kingdom = models.CharField(_("界"), max_length=50,null=True, blank=True)
    taxon_kingdom_chinese = models.CharField(_("界_中文"), max_length=50,null=True, blank=True)
    taxon_phylum = models.CharField(_("门"), max_length=50,null=True, blank=True)
    taxon_phylum_chinese = models.CharField(_("门_中文"), max_length=50,null=True, blank=True)
    taxon_class = models.CharField(_("纲"), max_length=50,null=True, blank=True)
    taxon_class_chinese = models.CharField(_("纲_中文"), max_length=50,null=True, blank=True)
    taxon_order = models.CharField(_("目"), max_length=50,null=True, blank=True)
    taxon_order_chinese = models.CharField(_("目_中文"), max_length=50,null=True, blank=True)
    taxon_family = models.CharField(_("科"), max_length=50,null=True, blank=True)
    taxon_family_chinese = models.CharField(_("科_中文"), max_length=50,null=True, blank=True)
    taxon_genus = models.CharField(_("属"), max_length=50,null=True, blank=True)
    taxon_genus_chinese = models.CharField(_("属_中文"), max_length=50,null=True, blank=True)
    taxon_species = models.CharField(_("种"), max_length=50,null=True, blank=True)
    taxon_species_chinese = models.CharField(_("种_中文"), max_length=50,null=True, blank=True)
    genomic_reference = models.CharField(_("参考基因组类型"), max_length=50,null=True, blank=True)
    data_origin = models.CharField(_("数据来源"), max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜_物种参考基因组'
        verbose_name_plural = '蜂蜜_物种参考基因组'

    def __str__(self):
        return f'{self.taxon_id}-{self.taxon_species}-{self.taxon_species_chinese}'


class HoneySample(models.Model):
    exact_site = models.CharField(_("简要采集地信息"), max_length=250 ,null=True, blank=True)
    surrounding_environment = models.CharField(_("周边环境"), max_length=50,null=True, blank=True)
    longitude = models.FloatField(_("经度"),null=True, blank=True)
    latitude = models.FloatField(_("纬度"),null=True, blank=True)
    altitude = models.IntegerField(_("海拔"),null=True, blank=True)
    honey_bee_origin = models.CharField(_("蜂种"), max_length=50,null=True, blank=True)
    honey_type = models.CharField(_("蜂蜜类型"), max_length=50,null=True, blank=True)
    honey_sample_note = models.TextField(_("样本备注"),null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜_样品'
        verbose_name_plural = '蜂蜜_样品'

    def __str__(self):
        return f'{self.exact_site}-{self.honey_type}'
