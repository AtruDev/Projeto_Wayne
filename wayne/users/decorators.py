from django.shortcuts import redirect
from django.contrib import messages

def role_required(roles):

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role not in roles:
                messages.error(request, "Você não tem permissão para acessar esta página.")
                return redirect('listar_recursos')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
