from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('consulta_api', views.consulta_api, name='consulta_api')
]