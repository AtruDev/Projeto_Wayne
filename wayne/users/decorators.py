from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

def role_required(roles):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role not in roles:
                messages.error(request, "Você não tem permissão para acessar esta página.")
                return redirect('resources:listar_recursos')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

def funcionario_required(view_func):
    return role_required(['funcionario', 'gerente', 'admin'])(view_func)

def gerente_required(view_func):
    return role_required(['gerente', 'admin'])(view_func)

def admin_required(view_func):
    return role_required(['admin'])(view_func)