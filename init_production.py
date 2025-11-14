#!/usr/bin/env python
import os
import sys

print("🚀 Configurando aplicación Django...")

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')

import django
django.setup()

from django.core.management import call_command, execute_from_command_line

try:
    print("🗄️ Configurando base de datos SQLite...")
    
    # Eliminar base de datos anterior si existe
    db_path = 'db.sqlite3'
    if os.path.exists(db_path):
        os.remove(db_path)
        print("🧹 Base de datos anterior eliminada")
    
    # Crear nuevas migraciones si es necesario
    print("📋 Creando migraciones...")
    call_command('makemigrations', verbosity=1)
    
    # Aplicar todas las migraciones
    print("⚡ Aplicando migraciones...")
    call_command('migrate', verbosity=2)
    
    # Verificar que las tablas se crearon
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in cursor.fetchall()]
        print(f"📊 Tablas creadas: {tables}")
    
    # Crear superusuario
    print("👤 Creando superusuario...")
    from django.contrib.auth.models import User
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@tienda.com', 'admin123')
        print("✅ Superusuario creado: admin/admin123")
    
    # Poblar datos de ejemplo
    print("📦 Poblando datos...")
    from tienda.models import Categoria, Producto
    
    if not Categoria.objects.exists():
        call_command('poblar_datos')
        print(f"✅ Categorías: {Categoria.objects.count()}")
        print(f"✅ Productos: {Producto.objects.count()}")
    
    print("🎉 ¡Configuración exitosa!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)