#!/usr/bin/env python
"""
Script de inicialización para Railway que se ejecuta antes del servidor
"""
import os
import sys
import django
from django.core.management import execute_from_command_line
from django.core.management.base import CommandError

def run_command(command_args):
    """Ejecuta un comando de Django y maneja errores"""
    try:
        print(f"🚀 Ejecutando: {' '.join(command_args)}")
        execute_from_command_line(command_args)
        print(f"✅ Completado: {' '.join(command_args)}")
        return True
    except CommandError as e:
        print(f"❌ Error en {' '.join(command_args)}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado en {' '.join(command_args)}: {e}")
        return False

def main():
    """Función principal de inicialización"""
    print("🔧 Iniciando configuración de Railway...")
    
    # Configurar Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')
    
    try:
        django.setup()
        print("✅ Django configurado correctamente")
    except Exception as e:
        print(f"❌ Error configurando Django: {e}")
        sys.exit(1)
    
    # Verificar base de datos
    from django.db import connection
    from django.conf import settings
    
    try:
        db_info = settings.DATABASES['default']
        print(f"📊 Base de datos: {db_info['ENGINE']}")
        if 'NAME' in db_info:
            print(f"📊 Archivo/Host: {db_info['NAME']}")
        
        # Probar conexión
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✅ Conexión a base de datos exitosa")
    except Exception as e:
        print(f"⚠️ Error de conexión a base de datos: {e}")
        print("🔄 Continuando con configuración...")
    
    # Ejecutar migraciones
    print("\n📦 Ejecutando migraciones...")
    
    # Ejecutar migraciones directamente
    print("🔄 Ejecutando migrate...")
    if run_command(['manage.py', 'migrate']):
        print("✅ Migraciones completadas")
    else:
        print("❌ Error en migrate - intentando crear tablas manualmente")
        run_command(['manage.py', 'migrate', '--run-syncdb'])
    
    # Poblar datos básicos
    print("\n📝 Poblando datos...")
    run_command(['manage.py', 'poblar_datos'])
    
    # Recolectar archivos estáticos
    print("\n🎨 Recolectando archivos estáticos...")
    run_command(['manage.py', 'collectstatic', '--noinput'])
    
    print("\n🎉 Inicialización completa!")
    print("🚀 Script terminado - Gunicorn iniciará automáticamente")

if __name__ == '__main__':
    main()