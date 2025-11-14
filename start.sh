#!/bin/bash

# Script de inicio para Railway
echo "🚀 Iniciando aplicación Django..."

# Ejecutar migraciones
echo "📦 Ejecutando migraciones..."
python manage.py migrate --noinput

# Crear superusuario si no existe
echo "👤 Configurando superusuario..."
python -c "
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@tienda.com', 'admin123')
    print('✅ Superusuario creado: admin/admin123')
else:
    print('✅ Superusuario ya existe')
"

# Poblar datos si no existen
echo "📋 Verificando datos iniciales..."
python -c "
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')
django.setup()

from tienda.models import Categoria, Producto

if not Categoria.objects.exists():
    from django.core.management import call_command
    call_command('poblar_datos')
    print('✅ Datos iniciales creados')
else:
    print('✅ Datos ya existen')
"

# Recolectar archivos estáticos
echo "📁 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🎉 ¡Aplicación lista!"

# Iniciar servidor
exec gunicorn Final.wsgi:application --bind 0.0.0.0:$PORT