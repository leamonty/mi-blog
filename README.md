
# Mi Blog

Aplicación web desarrollada con Python y Django que permite a los usuarios registrarse, iniciar sesión y gestionar publicaciones.

## Funcionalidades

- Registro de usuarios.
- Inicio y cierre de sesión.
- Listado de publicaciones.
- Visualización individual de cada publicación.
- Creación de publicaciones para usuarios autenticados.
- Edición y eliminación de publicaciones propias.
- Control de permisos: cada usuario puede modificar o eliminar únicamente sus publicaciones.
- Carga de imágenes en las publicaciones.

## Tecnologías utilizadas

- Python 3.14
- Django 6.1
- SQLite
- Pillow
- python-dotenv
- HTML y CSS

## Requisitos

- Python 3.14 o compatible.
- Git.
- pip.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/leamonty/mi-blog.git
cd mi-blog
```

### 2. Crear y activar un entorno virtual

En Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Crear una copia del archivo de ejemplo `.env.example` y nombrarla `.env`.

En Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

En Linux o macOS:

```bash
cp .env.example .env
```

Editar `.env` y reemplazar el valor de `SECRET_KEY` por una clave secreta propia. Se puede generar una nueva con:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Mantener `DEBUG=True` únicamente para desarrollo local.

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Panel de administración

Para acceder al panel administrativo:

```bash
python manage.py createsuperuser
```

Luego ingresar en:

http://127.0.0.1:8000/admin/

## Archivos y datos locales

La base de datos SQLite (`db.sqlite3`), las imágenes cargadas (`media/`), el entorno virtual (`venv/`) y el archivo `.env` son locales y no forman parte del repositorio.

Al realizar una instalación nueva, Django crea una base de datos vacía al ejecutar las migraciones.

## Autor

Leandro Montenegro

GitHub: [@leamonty](https://github.com/leamonty)
