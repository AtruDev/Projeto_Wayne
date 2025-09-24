from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    """
    Carrega automaticamente o initial_data.json após o migrate.
    """
    if sender.name == "users":
        try:
            call_command("loaddata", "fixtures/initial_data.json")
            print("✔ Dados iniciais carregados com sucesso!")
        except Exception as e:
            print(f"⚠ Não foi possível carregar dados iniciais: {e}")
