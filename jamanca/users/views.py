from django.db.utils import OperationalError
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from .models import Icono, Perfil, Persona, Rol, RolPermiso


def _bd_lista(request, template, contexto, obtener_filas):
    try:
        filas = obtener_filas()
        contexto["filas"] = filas
        contexto["total"] = len(filas)
        return render(request, template, contexto)
    except OperationalError:
        return render(
            request,
            "setup_required.html",
            {"titulo": contexto.get("titulo", "Módulo")},
        )


def _conteos():
    return {
        "total_personas": Persona.objects.count(),
        "total_roles": Rol.objects.count(),
        "total_perfiles": Perfil.objects.count(),
        "total_iconos": Icono.objects.count(),
        "total_rol_permisos": RolPermiso.objects.count(),
    }


@never_cache
def dashboard(request):
    try:
        return render(request, "dashboard.html", _conteos())
    except OperationalError:
        return render(request, "setup_required.html", {"titulo": "Panel Principal"})


@never_cache
def personas(request):
    return _bd_lista(
        request,
        "personas.html",
        {
            "titulo": "Personas",
            "subtitulo": "Datos civiles (DNI, nombres)",
            "badge_icon": "bi-people-fill",
            "columnas": ["DNI", "Nombres", "Apellidos"],
            "table_id": "table_personas",
            "search_id": "search_personas",
        },
        lambda: [(p.dni, p.nombres, p.apellidos or "—") for p in Persona.objects.all()],
    )


@never_cache
def roles(request):
    return _bd_lista(
        request,
        "roles.html",
        {
            "titulo": "Roles",
            "subtitulo": "Niveles de acceso y etiquetas",
            "badge_icon": "bi-shield-lock-fill",
            "columnas": ["Nombre", "Descripción"],
            "table_id": "table_roles",
            "search_id": "search_roles",
        },
        lambda: [(r.nombre, r.descripcion or "—") for r in Rol.objects.all()],
    )


@never_cache
def perfiles(request):
    return _bd_lista(
        request,
        "perfiles.html",
        {
            "titulo": "Perfiles",
            "subtitulo": "Extensión de auth_user con persona y rol",
            "badge_icon": "bi-person-badge-fill",
            "columnas": ["Usuario", "Persona", "Rol"],
            "table_id": "table_perfiles",
            "search_id": "search_perfiles",
        },
        lambda: [
            (p.usuario.username, str(p.persona), p.rol.nombre)
            for p in Perfil.objects.select_related("usuario", "persona", "rol")
        ],
    )


@never_cache
def iconos(request):
    return _bd_lista(
        request,
        "iconos.html",
        {
            "titulo": "Iconos",
            "subtitulo": "Recursos visuales del sistema",
            "badge_icon": "bi-palette-fill",
            "columnas": ["Nombre", "Clase CSS / Ruta"],
            "table_id": "table_iconos",
            "search_id": "search_iconos",
        },
        lambda: [(i.nombre, i.clase_css or "—") for i in Icono.objects.all()],
    )


@never_cache
def rol_permisos(request):
    return _bd_lista(
        request,
        "rol_permisos.html",
        {
            "titulo": "Permisos por Rol",
            "subtitulo": "Tabla users_rolpermiso (rol + permiso + icono)",
            "badge_icon": "bi-key-fill",
            "columnas": ["Rol", "Permiso Django", "Icono"],
            "table_id": "table_rol_permisos",
            "search_id": "search_rol_permisos",
        },
        lambda: [
            (rp.rol.nombre, rp.permiso.name, rp.icono.nombre if rp.icono else "—")
            for rp in RolPermiso.objects.select_related("rol", "permiso", "icono")
        ],
    )
