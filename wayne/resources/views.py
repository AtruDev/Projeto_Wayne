from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_recursos(request):
    recursos = Resource.objects.all()
    return render(request, 'resources/listar.html', {'recursos': recursos})

def criar_recurso(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("resources:listar_recursos")
    else:
        form = ResourceForm()
    return render(request, 'resources/form.html', {'form': form, "acao":"Criar"})

def editar_recurso(request, pk):
    recurso = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect("resources:listar_recursos")
    else:
        form = ResourceForm(instance=recurso)
    return render(request, 'resources/form.html', {'form': form,"acao":"Editar"})

def deletar_recurso(request, pk):
    recurso = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        recurso.delete()
        return redirect("resources:listar_recursos")
    return render(request, 'resources/deletar.html', {'recurso': recurso})
