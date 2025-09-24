from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from users.views import CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resources/', include('resources.urls')),
    path("users/", include("users.urls")),
    path("dashboard/", include("dashboard.urls")),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login' ),
    path('accounts/logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),
    
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),

    path('', include('dashboard.urls')),
  
]
