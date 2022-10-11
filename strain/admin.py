from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import StrainOrigin, Taxonomy, Sequencing16s, GenomeInfo,Isolate, Storage, StrainAll


@admin.register(StrainOrigin)
class StrainOriginAdmin(ImportExportModelAdmin):
    pass

@admin.register(Taxonomy)
class TaxonomyAdmin(ImportExportModelAdmin):
    pass


@admin.register(Sequencing16s)
class Sequencing16sAdmin(ImportExportModelAdmin):
    pass

@admin.register(GenomeInfo)
class GenomeInfoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Isolate)
class IsolateAdmin(ImportExportModelAdmin):
    pass

@admin.register(Storage)
class StorageAdmin(ImportExportModelAdmin):
    pass

@admin.register(StrainAll)
class StrainAllAdmin(ImportExportModelAdmin):
    pass
