from .models import BeeAll
import django_filters

class BeeAllFilter(django_filters.FilterSet):
    class Meta:
        model = BeeAll
        fields = ['gut_storage','gut_usage','headthorax_preservation','headthorax_usage',
                 'abdomen_preservation','abdomen_usage','leg_storage','leg_usage']