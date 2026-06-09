# Práctica Calificada 02 — Django (Jamanca)

Proyecto según la evaluación PDF y el diagrama ER (`users_*`).

## Estructura

```
practica_calificada_02/
├── venv/
├── requirements.txt
└── jamanca/
    ├── manage.py
    ├── db.sqlite3          (se crea al migrar)
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   ├── personas.html
    │   ├── roles.html
    │   ├── perfiles.html
    │   ├── iconos.html
    │   └── rol_permisos.html
    ├── jamanca/
    │   ├── settings.py
    │   └── urls.py
    └── users/
        ├── models.py
        ├── urls.py
        ├── views.py
        └── migrations/
```

## Cómo ejecutar (PowerShell)

**Primera vez** (crear tablas y datos):

```powershell
cd "c:\Users\lucas\OneDrive\Documentos\2026\practica_calificada_02\jamanca"
..\venv\Scripts\activate
python manage.py setup_proyecto
```

**Cada vez que trabajes** (servidor):

```powershell
cd "c:\Users\lucas\OneDrive\Documentos\2026\practica_calificada_02\jamanca"
..\venv\Scripts\activate
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

### Comandos por separado (opcional)

```powershell
python manage.py migrate
python manage.py load_demo_data
python manage.py runserver
```

## Base de datos (diagrama ER)

| Tabla | Modelo |
|-------|--------|
| `users_persona` | Persona |
| `users_rol` | Rol |
| `users_perfil` | Perfil → OneToOne `auth_user` |
| `users_icono` | Icono |
| `users_rolpermiso` | RolPermiso |

**Admin:** http://127.0.0.1:8000/admin/ — usuario `admin`, clave `admin123`

## Requisitos PDF

- App `users` en `INSTALLED_APPS`
- Modelos según diagrama + migraciones
- Rutas en `users/urls.py` (incluidas desde `jamanca/urls.py`)
- Panel con navegación cíclica entre módulos
