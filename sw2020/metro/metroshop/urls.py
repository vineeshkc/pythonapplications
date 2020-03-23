from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('master_config', views.master_config, name='master_config'),
    path('master_config_update2', views.master_config_update2, name='master_config_update2'),

]