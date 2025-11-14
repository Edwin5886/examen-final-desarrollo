#!/usr/bin/env python
"""
Script para ejecutar migraciones y poblar datos iniciales en producción
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')
django.setup()

from django.core.management import call_command
from django.db import connection

def main():
    """Función principal para setup de producción"""
    print("🚀 Configurando aplicación para producción...")
    
    # Ejecutar migraciones
    print("📦 Ejecutando migraciones...")
    call_command('migrate', verbosity=1)
    
    # Crear superusuario si no existe
    print("👤 Verificando superusuario...")
    from django.contrib.auth.models import User
    if not User.objects.filter(is_superuser=True).exists():
        print("Creando superusuario admin...")
        User.objects.create_superuser(
            username='admin',
            email='admin@tienda.com',
            password='admin123'
        )
        print("✅ Superusuario creado: admin/admin123")
    
    # Poblar datos iniciales solo si no existen
    print("📋 Verificando datos iniciales...")
    from tienda.models import Categoria, Producto
    
    if not Categoria.objects.exists() or not Producto.objects.exists():
        print("Poblando datos iniciales...")
        try:
            call_command('poblar_datos')
            print("✅ Datos iniciales creados")
        except Exception as e:
            print(f"⚠️ Error poblando datos: {e}")
    else:
        print("✅ Datos ya existen")
    
    # Recolectar archivos estáticos
    print("📁 Recolectando archivos estáticos...")
    call_command('collectstatic', '--noinput', verbosity=1)
    
    print("🎉 ¡Configuración completada!")

if __name__ == '__main__':
    main()