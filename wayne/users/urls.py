from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.listar_usuarios, name="listar_usuarios"),
    path("create/", views.criar_usuario, name="criar_usuario"),
    path("<int:pk>/edit/", views.editar_usuario, name="editar_usuario"),
    path("<int:pk>/delete/", views.deletar_usuario, name="deletar_usuario"),
]
