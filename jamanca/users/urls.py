from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("personas/", views.personas, name="personas"),
    path("roles/", views.roles, name="roles"),
    path("perfiles/", views.perfiles, name="perfiles"),
    path("iconos/", views.iconos, name="iconos"),
    path("rol-permisos/", views.rol_permisos, name="rol_permisos"),
]
