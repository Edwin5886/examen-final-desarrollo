# 🛒 Tienda Virtual - Proyecto Final Django

Una aplicación web de e-commerce desarrollada con Django que incluye gestión de productos y categorías.

## ✨ Características

- 🏠 Página de inicio con productos destacados
- 📦 Gestión completa de productos (CRUD)
- 🏷️ Gestión de categorías con iconos FontAwesome
- 💰 Precios en Quetzales guatemaltecos (Q)
- 📱 Diseño responsive con Bootstrap 5
- 🔧 Panel de administración Django

## 🚀 Despliegue en Railway

### Prerrequisitos

1. Cuenta en [Railway](https://railway.app/)
2. Cuenta en [GitHub](https://github.com/)

### Pasos para desplegar

#### 1. Subir código a GitHub

```bash
# Inicializar repositorio Git
git init

# Agregar archivos
git add .

# Hacer commit
git commit -m "Proyecto Django Tienda Virtual"

# Agregar repositorio remoto (reemplaza con tu URL)
git remote add origin https://github.com/TU_USUARIO/tienda-virtual.git

# Subir código
git push -u origin main
```

#### 2. Desplegar en Railway

1. Ve a [Railway](https://railway.app/) y crea una cuenta
2. Haz clic en "New Project"
3. Selecciona "Deploy from GitHub repo"
4. Conecta tu repositorio
5. Railway detectará automáticamente que es un proyecto Django

#### 3. Configurar variables de entorno

En el dashboard de Railway, ve a "Variables" y agrega:

```
SECRET_KEY=tu-clave-secreta-muy-segura-aqui
DEBUG=False
```

#### 4. Configurar base de datos

1. En Railway, agrega un servicio PostgreSQL
2. Railway generará automáticamente la variable `DATABASE_URL`

#### 5. Configurar dominio personalizado (opcional)

1. Ve a "Settings" > "Domains"
2. Agrega tu dominio personalizado o usa el generado por Railway

## 🔧 Comandos útiles

```bash
# Instalar dependencias localmente
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Poblar datos de ejemplo
python manage.py poblar_datos

# Ejecutar servidor de desarrollo
python manage.py runserver
```

## 📂 Estructura del proyecto

```
Final/
├── Final/              # Configuración principal
│   ├── settings.py     # Configuración Django
│   ├── urls.py        # URLs principales
│   └── wsgi.py        # WSGI para producción
├── tienda/            # App principal
│   ├── models.py      # Modelos de datos
│   ├── views.py       # Vistas
│   ├── urls.py        # URLs de la app
│   ├── forms.py       # Formularios
│   └── templates/     # Plantillas HTML
├── static/            # Archivos estáticos
├── media/             # Archivos subidos
├── requirements.txt   # Dependencias
├── Procfile          # Configuración Railway
└── runtime.txt       # Versión de Python
```

## 🎨 Tecnologías utilizadas

- **Backend**: Django 5.2.8
- **Frontend**: Bootstrap 5, FontAwesome
- **Base de datos**: SQLite (desarrollo), PostgreSQL (producción)
- **Despliegue**: Railway
- **Servidor web**: Gunicorn + WhiteNoise

## 👤 Credenciales por defecto

- **Admin**: admin / admin123
- **Panel admin**: `/admin/`

## 🔗 Enlaces importantes

- **Aplicación en vivo**: [Tu URL de Railway aquí]
- **Panel de administración**: [Tu URL]/admin/
- **Repositorio**: [Tu URL de GitHub aquí]

## 📝 Notas

- Los archivos de media se almacenan localmente (para producción real considera usar S3)
- La base de datos se puebla automáticamente con datos de ejemplo
- El proyecto está configurado para usar PostgreSQL en producción y SQLite en desarrollo

---

Desarrollado como proyecto final para el curso de Desarrollo Web con Django.