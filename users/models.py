from django.contrib.auth.models import AbstractUser 
from django.db import models

class User(AbstractUser):
    ROLE_FUNC = 'funcionario'
    ROLE_GER = 'gerente'
    ROLE_ADM = 'admin'

    ROLE_CHOICES = (
        (ROLE_FUNC, 'funcionário'),
        (ROLE_GER, 'Gerente'),
        (ROLE_ADM, 'Adiministrador'),
    )

    role = models.CharField(
        max_length = 20,
        choices = ROLE_CHOICES,
        default = ROLE_FUNC 
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"