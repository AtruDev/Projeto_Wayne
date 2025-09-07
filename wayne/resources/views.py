from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resource
from users.decorators import role_required

@login_required
def listar_recursos(request):
    recursos = Resource.objects.all()
    return render(request, "resources/listar.html", {"recursos" : recursos})

@role_required(['gerente', 'admin'])
def criar_recurso(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        descricao = request.POST.get("descricao")
        Resource.objects.create(nome=nome, tipo=tipo, descricao=descricao)
        return redirect("listar_recursos")
    return render(request, "resources/criar.html")

@role_required(['gerente', 'admin'])
def editar_recurso(request, id):
    recurso = get_object_or_404(Resource, id=id)
    if request.method == "POST":
        recurso.nome = request.POST.get("nome")
        recurso.tipo = request.POST.get("tipo")
        recurso.descricao = request.POST.get("descricao")
        recurso.save()
        return redirect("listar_recursos")
    return render(request, "resources/editar.html", {"recurso": recurso})

@role_required(['admin'])
def deletar_recurso(request, id):
    recurso = get_object_or_404(Resource, id=id)
    if request.method == "Post":
        recurso.delete()
        return redirect("listar+recursos")
    return render(request, "resources/deletar.html", {"recurso": recurso})