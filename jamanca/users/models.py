from django.contrib.auth.models import Permission, User
from django.db import models


class Persona(models.Model):
    """Datos civiles: DNI, nombres."""

    dni = models.CharField(max_length=8, unique=True, verbose_name="DNI")
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.dni} - {self.nombres} {self.apellidos}".strip()


class Rol(models.Model):
    """Niveles de acceso y etiquetas del sistema."""

    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Icono(models.Model):
    """Recursos visuales del sistema."""

    nombre = models.CharField(max_length=50)
    clase_css = models.CharField(
        max_length=80,
        blank=True,
        help_text="Clase de icono (ej. bi-person) o ruta de imagen",
    )

    class Meta:
        verbose_name = "Icono"
        verbose_name_plural = "Iconos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    """Extensión de auth_user; vincula usuario con Persona y Rol."""

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil",
    )
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name="perfiles",
    )
    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        related_name="perfiles",
    )

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


class RolPermiso(models.Model):
    """Asignación dinámica de permisos Django a roles."""

    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE,
        related_name="rol_permisos",
    )
    permiso = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="rol_permisos",
    )
    icono = models.ForeignKey(
        Icono,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rol_permisos",
    )

    class Meta:
        verbose_name = "Permiso de rol"
        verbose_name_plural = "Permisos de rol"
        unique_together = ("rol", "permiso")

    def __str__(self):
        return f"{self.rol} → {self.permiso.codename}"
