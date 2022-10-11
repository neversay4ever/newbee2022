from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import CollectionData, Taxonomy, SpecimenDetails, HeadthoraxStorage,AbdomenStorage,GutStorage,LegStorage,BeeAll

@admin.register(CollectionData)
class CollectionDataAdmin(ImportExportModelAdmin):
    pass

@admin.register(Taxonomy)
class TaxonomyAdmin(ImportExportModelAdmin):
    pass

@admin.register(SpecimenDetails)
class SpecimenDetailsAdmin(ImportExportModelAdmin):
    pass

@admin.register(HeadthoraxStorage)
class HeadthoraxStorageAdmin(ImportExportModelAdmin):
    pass

@admin.register(AbdomenStorage)
class AbdomenStorageAdmin(ImportExportModelAdmin):
    pass

@admin.register(GutStorage)
class GutStorageaAdmin(ImportExportModelAdmin):
    pass

@admin.register(LegStorage)
class LegStorageAdmin(ImportExportModelAdmin):
    pass

@admin.register(BeeAll)
class BeeAllAdmin(ImportExportModelAdmin):
    pass