from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crea las tablas (migrate) y carga datos de demostración"

    def handle(self, *args, **options):
        self.stdout.write("Aplicando migraciones...")
        call_command("migrate", verbosity=1)
        self.stdout.write("Cargando datos de demostración...")
        call_command("load_demo_data", verbosity=1)
        self.stdout.write(
            self.style.SUCCESS(
                "Listo. Inicie el servidor con: python manage.py runserver"
            )
        )
