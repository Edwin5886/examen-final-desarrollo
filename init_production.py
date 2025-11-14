#!/usr/bin/env python
import os
import sys
import django

print("🚀 Iniciando configuración de producción...")

# Configurar settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')

# Inicializar Django
django.setup()

from django.core.management import call_command
from django.db import connection

try:
    # Crear todas las tablas desde cero
    print("📋 Creando tablas de base de datos...")
    
    # Ejecutar migraciones forzadas
    call_command('migrate', '--run-syncdb', verbosity=2)
    
    print("✅ Tablas creadas exitosamente")
    
    # Verificar que las tablas existen
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"📊 Tablas encontradas: {[table[0] for table in tables]}")
    
    # Importar modelos después de crear tablas
    from django.contrib.auth.models import User
    from tienda.models import Categoria, Producto
    
    # Crear superusuario
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@tienda.com', 'admin123')
        print("👤 Superusuario creado: admin/admin123")
    
    # Poblar datos de ejemplo
    if not Categoria.objects.exists():
        call_command('poblar_datos')
        print("📦 Datos de ejemplo creados")
        
        # Verificar datos
        print(f"✅ Categorías creadas: {Categoria.objects.count()}")
        print(f"✅ Productos creados: {Producto.objects.count()}")
    else:
        print("📦 Datos ya existen")
    
    print("🎉 ¡Configuración completada exitosamente!")
    
except Exception as e:
    print(f"❌ Error durante la configuración: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)