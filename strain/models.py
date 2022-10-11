from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class StrainOrigin(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    bee_host_species = models.CharField(_("蜜蜂宿主物种"), max_length=50, null=True, blank=True)
    exact_site = models.CharField(_("采集地简要信息"), max_length=50, null=True, blank=True)
    bee_host_id= models.CharField(_("蜜蜂宿主样本编号"), max_length=50, null=True, blank=True)
    gut_id = models.CharField(_("肠道样本编号"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_来源'
        verbose_name_plural = '菌株_来源'
    
    def __str__(self):
        return f'{self.strain_id}-{self.exact_site}'


class Taxonomy(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    strain_phylum = models.CharField(_("菌门"), max_length=50, null=True, blank=True)
    strain_class = models.CharField(_("菌纲"), max_length=50, null=True, blank=True)
    strain_order = models.CharField(_("菌目"), max_length=50, null=True, blank=True)
    strain_family = models.CharField(_("菌科"), max_length=50, null=True, blank=True)
    strain_genus = models.CharField(_("菌属"), max_length=50, null=True, blank=True)
    strain_species = models.CharField(_("菌种"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_分类'
        verbose_name_plural = '菌株_分类'

    def __str__(self):
        return f'{self.strain_id}-{self.strain_species}'

class Sequencing16s(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    ab1_quality_16s = models.CharField(_("16S测序质量"), max_length=50, null=True, blank=True)
    mapped_sequence_16s = models.CharField(_("16S比对到的序列"), max_length=250, null=True, blank=True)
    similarity_16s = models.FloatField(_("16S比对相似度"), null=True, blank=True)
    blast_website_16s = models.CharField(_("16S比对网站"), max_length=250, null=True, blank=True)
    data_file_path_16s = models.CharField(_("16S序列存储位置"), max_length=250, null=True, blank=True)
    blast_by_who_16s = models.CharField(_("16S比对人员"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_16S比对信息'
        verbose_name_plural = '菌株_16S比对信息'
    
    def __str__(self):
        return f'{self.strain_id}-{self.mapped_sequence_16s}'


class GenomeInfo(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    strain_genome_sequence = models.CharField(_("是否检测细菌基因组"), max_length=50, null=True, blank=True)
    strain_genome_seq_id = models.CharField(_("细菌基因组测序编号"), max_length=150, null=True, blank=True)
    strain_genome_server_site = models.CharField(_("细菌基因组序列在服务器中的存储位置"), max_length=250, null=True, blank=True)
    strain_NCBI_accession = models.CharField(_("细菌基因组上传NCBI的accession号"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_基因组信息'
        verbose_name_plural = '菌株_基因组信息'

    def __str__(self):
        return f'{self.strain_id}-{self.strain_genome_sequence}'

class Isolate(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    isolation_id = models.CharField(_("分离株编号"), max_length=50, null=True, blank=True)
    isolation_media = models.CharField(_("菌株分离培养基"), max_length=50, null=True, blank=True)
    isolation_culture_type = models.CharField(_("菌株分离培养类型"), max_length=50, null=True, blank=True)
    isolation_culture_temperature = models.CharField(_("菌株分离培养温度"), max_length=50, null=True, blank=True)
    isolation_culture_time_hour = models.CharField(_("菌株分离培养时间"), max_length=50, null=True, blank=True)
    isolation_phenotype = models.CharField(_("分离株表型"), max_length=50, null=True, blank=True)
    isolate_by_who = models.CharField(_("菌株分离培养人员"), max_length=50, null=True, blank=True)
    isolation_record_by_who = models.CharField(_("菌株分离培养记录人员"), max_length=50, null=True, blank=True)
    isolation_record_date = models.DateField(_("菌株分离培养记录时间"), auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_分离培养信息'
        verbose_name_plural = '菌株_分离培养信息'

    def __str__(self):
        return f'{self.strain_id}-{self.isolation_id}-{self.isolation_record_by_who}'


class Storage(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    strain_storage_box_id = models.CharField(_("菌株存储盒子编号"), max_length=50, null=True, blank=True)
    strain_storage_solution = models.CharField(_("菌株储存液"), max_length=50, null=True, blank=True)
    strain_storage_temperature_centigrade = models.CharField(_("菌株储存温度"), max_length=50, null=True, blank=True)
    strain_storage_location = models.CharField(_("菌株储存地点"), max_length=50, null=True, blank=True)
    strain_storage_date = models.DateField(_("菌株储存时间"), auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_储存信息'
        verbose_name_plural = '菌株_储存信息'

    def __str__(self):
        return f'{self.strain_id}-{self.strain_storage_location}'


class StrainAll(models.Model):
    strain_id = models.CharField(_("菌株编号"), max_length=50, null=True, blank=True)
    bee_host_species = models.CharField(_("蜜蜂宿主物种"), max_length=50, null=True, blank=True)
    exact_site = models.CharField(_("采集地简要信息"), max_length=50, null=True, blank=True)
    bee_host_id= models.CharField(_("蜜蜂宿主样本编号"), max_length=50, null=True, blank=True)
    gut_id = models.CharField(_("肠道样本编号"), max_length=50, null=True, blank=True)

    strain_phylum = models.CharField(_("菌门"), max_length=50, null=True, blank=True)
    strain_class = models.CharField(_("菌纲"), max_length=50, null=True, blank=True)
    strain_order = models.CharField(_("菌目"), max_length=50, null=True, blank=True)
    strain_family = models.CharField(_("菌科"), max_length=50, null=True, blank=True)
    strain_genus = models.CharField(_("菌属"), max_length=50, null=True, blank=True)
    strain_species = models.CharField(_("菌种"), max_length=50, null=True, blank=True)

    ab1_quality_16s = models.CharField(_("16S测序质量"), max_length=50, null=True, blank=True)
    mapped_sequence_16s = models.CharField(_("16S比对到的序列"), max_length=250, null=True, blank=True)
    similarity_16s = models.FloatField(_("16S比对相似度"), null=True, blank=True)
    blast_website_16s = models.CharField(_("16S比对网站"), max_length=250, null=True, blank=True)
    data_file_path_16s = models.CharField(_("16S序列存储位置"), max_length=250, null=True, blank=True)
    blast_by_who_16s = models.CharField(_("16S比对人员"), max_length=50, null=True, blank=True)

    strain_genome_sequence = models.CharField(_("是否检测细菌基因组"), max_length=50, null=True, blank=True)
    strain_genome_seq_id = models.CharField(_("细菌基因组测序编号"), max_length=150, null=True, blank=True)
    strain_genome_server_site = models.CharField(_("细菌基因组序列在服务器中的存储位置"), max_length=250, null=True, blank=True)
    strain_NCBI_accession = models.CharField(_("细菌基因组上传NCBI的accession号"), max_length=50, null=True, blank=True)

    isolation_id = models.CharField(_("分离株编号"), max_length=50, null=True, blank=True)
    isolation_media = models.CharField(_("菌株分离培养基"), max_length=50, null=True, blank=True)
    isolation_culture_type = models.CharField(_("菌株分离培养类型"), max_length=50, null=True, blank=True)
    isolation_culture_temperature = models.CharField(_("菌株分离培养温度"), max_length=50, null=True, blank=True)
    isolation_culture_time_hour = models.CharField(_("菌株分离培养时间"), max_length=50, null=True, blank=True)
    isolation_phenotype = models.CharField(_("分离株表型"), max_length=50, null=True, blank=True)
    isolate_by_who = models.CharField(_("菌株分离培养人员"), max_length=50, null=True, blank=True)
    isolation_record_by_who = models.CharField(_("菌株分离培养记录人员"), max_length=50, null=True, blank=True)
    isolation_record_date = models.DateField(_("菌株分离培养记录时间"), auto_now=False, auto_now_add=False, null=True, blank=True)

    strain_storage_box_id = models.CharField(_("菌株存储盒子编号"), max_length=50, null=True, blank=True)
    strain_storage_solution = models.CharField(_("菌株储存液"), max_length=50, null=True, blank=True)
    strain_storage_temperature_centigrade = models.CharField(_("菌株储存温度"), max_length=50, null=True, blank=True)
    strain_storage_location = models.CharField(_("菌株储存地点"), max_length=50, null=True, blank=True)
    strain_storage_date = models.DateField(_("菌株储存时间"), auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name = '菌株_总表'
        verbose_name_plural = '菌株_总表'

    def __str__(self):
        return f'{self.strain_id}-{self.exact_site}-{self.isolation_id}'
