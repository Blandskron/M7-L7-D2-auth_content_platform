# Plataforma de Autenticación y Gestión de Contenido (Apps Core Django)

## 1) Crear entorno virtual

```bash
python -m venv venv
```

## 2) Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 3) Actualizar pip

```bash
python -m pip install --upgrade pip
```

## 4) Instalar Django

```bash
pip install django
```

## 5) Crear proyecto

```bash
django-admin startproject auth_content_platform
```

## 6) Entrar al proyecto

```bash
cd auth_content_platform
```

## 7) Crear aplicación

```bash
python manage.py startapp core
```

## 8) Registrar apps y configuración base en `auth_content_platform/settings.py`

En `INSTALLED_APPS` dejar/confirmar e incluir:

```python
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'core',
```

Agregar/confirmar al final:

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = []

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
```

## 9) Conectar rutas del proyecto en `auth_content_platform/urls.py`

Editar para incluir:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

## 10) Crear archivos esenciales en la app `core`

Crear/editar los siguientes archivos y pegar el código correspondiente:

### `core/models.py`

* Modelo `ContentItem` con relación a `auth.User`
* Soporte `contenttypes` con `GenericForeignKey`

### `core/admin.py`

* Registro del modelo `ContentItem` en el Admin

### `core/views.py`

* Login / Logout (auth)
* Dashboard (auth + sessions + contenttypes)
* Listado y creación de contenidos (ORM)
* Inspección de modelos internos (User, Session, ContentType)

### `core/urls.py`

* Rutas para login/logout/dashboard/contents/inspect con nombres

## 11) Crear templates

Crear carpeta:

```text
core/templates/core/
```

Crear estos archivos y pegar el código correspondiente:

* `base.html`
* `login.html`
* `dashboard.html`
* `content_list.html`
* `model_inspection.html`

## 12) Crear migraciones

```bash
python manage.py makemigrations
```

## 13) Aplicar migraciones

```bash
python manage.py migrate
```

## 14) Crear superusuario para el Admin

```bash
python manage.py createsuperuser
```

## 15) Ejecutar servidor

```bash
python manage.py runserver
```

## 16) Rutas

* Login: `http://127.0.0.1:8000/login/`
* Dashboard: `http://127.0.0.1:8000/`
* Contenidos: `http://127.0.0.1:8000/contents/`
* Inspección modelos: `http://127.0.0.1:8000/inspect/`
* Admin: `http://127.0.0.1:8000/admin/`

## 17) Flujo de uso

1. Abrir `/admin/` y autenticar con el superusuario creado
2. Abrir `/login/` y autenticar
3. Abrir `/contents/` y crear contenido con el formulario (CSRF habilitado)
4. Abrir `/inspect/` para ver campos internos de modelos preinstalados (User, Session, ContentType)
