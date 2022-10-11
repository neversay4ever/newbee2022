from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import HoneyCollector, HoneyIngredients, HoneyRefGenome, HoneySample


@admin.register(HoneyCollector)
class HoneyCollectorAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneyIngredients)
class HoneyIngredientsAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneyRefGenome)
class HoneyRefGenomeAdmin(ImportExportModelAdmin):
    pass

@admin.register(HoneySample)
class HoneySampleAdmin(ImportExportModelAdmin):
    pass
