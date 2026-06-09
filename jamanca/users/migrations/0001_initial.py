import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Icono",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                (
                    "clase_css",
                    models.CharField(
                        blank=True,
                        help_text="Clase de icono (ej. bi-person) o ruta de imagen",
                        max_length=80,
                    ),
                ),
            ],
            options={
                "verbose_name": "Icono",
                "verbose_name_plural": "Iconos",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dni",
                    models.CharField(max_length=8, unique=True, verbose_name="DNI"),
                ),
                ("nombres", models.CharField(max_length=100)),
                ("apellidos", models.CharField(blank=True, max_length=100)),
            ],
            options={
                "verbose_name": "Persona",
                "verbose_name_plural": "Personas",
                "ordering": ["apellidos", "nombres"],
            },
        ),
        migrations.CreateModel(
            name="Rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
                ("descripcion", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "Rol",
                "verbose_name_plural": "Roles",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Perfil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "persona",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="perfiles",
                        to="users.persona",
                    ),
                ),
                (
                    "rol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="perfiles",
                        to="users.rol",
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="perfil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil",
                "verbose_name_plural": "Perfiles",
            },
        ),
        migrations.CreateModel(
            name="RolPermiso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "icono",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rol_permisos",
                        to="users.icono",
                    ),
                ),
                (
                    "permiso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rol_permisos",
                        to="auth.permission",
                    ),
                ),
                (
                    "rol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rol_permisos",
                        to="users.rol",
                    ),
                ),
            ],
            options={
                "verbose_name": "Permiso de rol",
                "verbose_name_plural": "Permisos de rol",
                "unique_together": {("rol", "permiso")},
            },
        ),
    ]
