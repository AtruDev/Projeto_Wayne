from django.db import models

class Resource(models.Model):
    TIPOS = [
        ('dispositivo', 'Dispositivo'),
        ('equipamento', 'Equipamento'),
        ('veiculo', 'Veículo'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
