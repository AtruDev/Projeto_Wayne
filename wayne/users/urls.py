from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.listar_usuarios, name="listar_usuarios"),
    path("criar/", views.criar_usuario, name="criar_usuario"),
    path("<int:user_id>/editar/", views.editar_usuario, name="editar_usuario"),
    path("<int:user_id>/deletar/", views.deletar_usuario, name="deletar_usuario"),
]
