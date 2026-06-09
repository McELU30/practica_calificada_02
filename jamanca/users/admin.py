from django.contrib import admin

from .models import Icono, Perfil, Persona, Rol, RolPermiso


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombres", "apellidos")
    search_fields = ("dni", "nombres", "apellidos")


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)


@admin.register(Icono)
class IconoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "clase_css")
    search_fields = ("nombre",)


class RolPermisoInline(admin.TabularInline):
    model = RolPermiso
    extra = 1


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "persona", "rol")
    list_filter = ("rol",)
    search_fields = ("usuario__username", "persona__dni", "persona__nombres")


@admin.register(RolPermiso)
class RolPermisoAdmin(admin.ModelAdmin):
    list_display = ("rol", "permiso", "icono")
    list_filter = ("rol",)
