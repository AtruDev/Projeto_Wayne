from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from resources.models import Resource

@login_required
def home(request):

    total_usuarios = User.objects.count()
    total_funcionarios = User.objects.filter(role="funcionario").count()
    total_gerentes = User.objects.filter(role="gerente").count()
    total_admins = User.objects.filter(role="admin").count()

    total_recursos = Resource.objects.count()
    recurso_por_tipo = Resource.objects.values("tipo").order_by("tipo").distinct()

    tipos = []
    quantidades = []
    for recurso in recurso_por_tipo:
        tipo = recurso["tipo"]
        quantidade = Resource.objects.filter(tipo=tipo).count()
        tipos.append(tipo)
        quantidades.append(quantidade)

    context = {
        "total_usuarios" : total_usuarios,
        "total_funcionarios" : total_funcionarios,
        "total_gerentes" : total_gerentes,
        "total_admins": total_admins,
        "total_recursos": total_recursos,
        "tipos": tipos,
        "quantidades": quantidades,
    }

    return render(request, "dashboard/home.html", context)
