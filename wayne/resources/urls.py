from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_recursos, name="listar_recursos"),
    path('criar/', views.criar_recurso, name="criar_recurso"),
    path('editar/<int:id>/', views.editar_recurso, name="editar_recurso"),
    path('deletar/<int:id>/', views.deletar_recurso, name="deletar_recurso"),
]