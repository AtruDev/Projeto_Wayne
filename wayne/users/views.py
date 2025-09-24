from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from users.decorators import role_required
from .forms import UserForm

@login_required
@role_required(["admin"])  # só admin pode ver usuários
def listar_usuarios(request):
    usuarios = User.objects.all().order_by("-criado_em")
    return render(request, "users/listar.html", {"usuarios": usuarios})

# CRIAR USUÁRIO
@login_required
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
    return render(request, "users/form.html", {"form": form, "acao": "Criar"})



# EDITAR USUÁRIO

@login_required
@role_required(["admin"])
def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect("users:listar_usuarios")
    else:
        form = UserForm(instance=usuario)
    return render(request, "users/form.html", {"form": form, "acao": "Editar"})



# DELETAR USUÁRIO

@login_required
@role_required(["admin"])
def deletar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        usuario.delete()
        messages.success(request, "Usuário removido com sucesso!")
        return redirect("users:listar_usuarios")
    return render(request, "users/deletar.html", {"usuario": usuario})
