from django.contrib.auth.models import Permission, User
from django.core.management.base import BaseCommand

from users.models import Icono, Perfil, Persona, Rol, RolPermiso


class Command(BaseCommand):
    help = "Carga datos de demostración para la práctica calificada"

    def handle(self, *args, **options):
        personas_data = [
            ("12345678", "Lucas", "García Pérez"),
            ("87654321", "María", "López Quispe"),
            ("11223344", "Carlos", "Ramírez Torres"),
        ]
        for dni, nombres, apellidos in personas_data:
            Persona.objects.get_or_create(
                dni=dni,
                defaults={"nombres": nombres, "apellidos": apellidos},
            )

        roles_data = [
            ("Administrador", "Acceso total al sistema"),
            ("Docente", "Gestión académica"),
            ("Estudiante", "Consulta y actividades propias"),
        ]
        roles = {}
        for nombre, descripcion in roles_data:
            rol, _ = Rol.objects.get_or_create(
                nombre=nombre,
                defaults={"descripcion": descripcion},
            )
            roles[nombre] = rol

        iconos_data = [
            ("Usuario", "bi-person"),
            ("Configuración", "bi-gear"),
            ("Reporte", "bi-file-text"),
        ]
        iconos = {}
        for nombre, clase in iconos_data:
            icono, _ = Icono.objects.get_or_create(
                nombre=nombre,
                defaults={"clase_css": clase},
            )
            iconos[nombre] = icono

        admin_user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@jamanca.edu.pe",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if created:
            admin_user.set_password("admin123")
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Usuario admin creado (clave: admin123)"))
        else:
            self.stdout.write("Usuario admin ya existía")

        docente_user, created = User.objects.get_or_create(
            username="docente",
            defaults={"email": "docente@jamanca.edu.pe", "is_staff": False},
        )
        if created:
            docente_user.set_password("docente123")
            docente_user.save()

        persona_admin = Persona.objects.get(dni="12345678")
        persona_docente = Persona.objects.get(dni="87654321")

        Perfil.objects.get_or_create(
            usuario=admin_user,
            defaults={"persona": persona_admin, "rol": roles["Administrador"]},
        )
        Perfil.objects.get_or_create(
            usuario=docente_user,
            defaults={"persona": persona_docente, "rol": roles["Docente"]},
        )

        perm_add = Permission.objects.filter(
            codename="add_user", content_type__app_label="auth"
        ).first()
        perm_view = Permission.objects.filter(
            codename="view_user", content_type__app_label="auth"
        ).first()
        if not perm_view:
            perm_view = Permission.objects.filter(
                codename="change_user", content_type__app_label="auth"
            ).first()

        if perm_add:
            RolPermiso.objects.get_or_create(
                rol=roles["Administrador"],
                permiso=perm_add,
                defaults={"icono": iconos["Usuario"]},
            )
        if perm_view:
            RolPermiso.objects.get_or_create(
                rol=roles["Docente"],
                permiso=perm_view,
                defaults={"icono": iconos["Reporte"]},
            )

        self.stdout.write(self.style.SUCCESS("Datos de demostración cargados correctamente."))
