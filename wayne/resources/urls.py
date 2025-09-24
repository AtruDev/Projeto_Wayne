from django.urls import path
from . import views

app_name = "resources"

urlpatterns = [
    path('', views.listar_recursos, name="listar_recursos"),
    path('criar/', views.criar_recurso, name="criar_recursos"),
    path('<int:pk>/editar/', views.editar_recurso, name="editar_recursos"),
    path('<int:pk>/deletar/', views.deletar_recurso, name="deletar_recursos"),
]