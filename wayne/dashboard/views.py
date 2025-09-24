from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import User
from resources.models import Resource
from django.db.models import Count

@login_required
def home(request):
    total_usuarios = User.objects.count()
    total_recursos = Resource.objects.count()

    # Agrupar recursos por tipo
    recursos_por_tipo = Resource.objects.values("tipo").annotate(total=Count("id"))
    tipos = [r["tipo"] for r in recursos_por_tipo]
    quantidades = [r["total"] for r in recursos_por_tipo]

     # Últimos registros
    ultimos_usuarios = User.objects.order_by("-id")[:5]
    ultimos_recursos = Resource.objects.order_by("-id")[:5]

    context = {
        "total_usuarios": total_usuarios,
        "total_recursos": total_recursos,
        "tipos": tipos,
        "quantidades": quantidades,
        "ultimos_usuarios": ultimos_usuarios,
        "ultimos_recursos": ultimos_recursos,
    }
    return render(request, "dashboard/home.html", context)
