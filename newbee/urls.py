"""newbee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bee import views as bee_views
from strain import views as strain_views
from honey import views as honey_views
from django.contrib import admin

admin.site.site_header = 'Bee&Honey&Strain管理系统'

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('bee/', bee_views.bee_home, name='bee_home'),
    path('bee_data_combine', bee_views.bee_data_combine, name='bee_data_combine'),
    path('bee/<str:sample_id>', bee_views.bee_single, name='bee_single'),
    path('sample_json/<str:data_string>', bee_views.getBeeJsonFromJstree, name='bee_selected_json'),

    path('honey/', honey_views.honey_home, name='honey_home'),
    
    path('strain/', strain_views.strain_home, name='strain_home'),
    path('strain_data_combine', strain_views.strain_data_combine, name='strain_data_combine'),
    path('strain/<str:strain_id>', strain_views.strain_single, name='strain_single'),

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

