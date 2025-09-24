from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserForm
from users.decorators import role_required
from django.contrib.auth.views import LogoutView

User = get_user_model()

@role_required(["admin"])
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, "users/listar.html", {"usuarios": usuarios})

@role_required(["admin"])
def criar_usuario(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect("users:listar_usuarios")
    else:
        form = UserForm()
    return render(request, "users/form.html", {"form": form, "titulo": "Criar Usuário"})

@role_required(["admin"])
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect("users:listar_usuarios")
    else:
        form = UserForm(instance=usuario)
    return render(request, "users/form.html", {"form": form, "titulo": "Editar Usuário"})

@role_required(["admin"])
def deletar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.delete()
    messages.success(request, "Usuário deletado com sucesso!")
    return redirect("users:listar_usuarios")

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Você saiu com sucesso!")
        return super().dispatch(request, *args, **kwargs)

    def get_next_page(self):
        return redirect("login").url