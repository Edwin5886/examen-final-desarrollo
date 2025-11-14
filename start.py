#!/usr/bin/env python
import os
import django
import subprocess
import sys

def run_cmd(cmd):
    print(f"🚀 Ejecutando: {cmd}")
    result = subprocess.run(cmd.split(), capture_output=True, text=True)
    print(f"📤 Salida: {result.stdout}")
    if result.stderr:
        print(f"⚠️ Error: {result.stderr}")
    return result.returncode == 0

print("🔧 ==> INICIANDO RAILWAY SETUP")

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')
django.setup()

print("✅ Django configurado")

# Migraciones
print("📦 ==> MIGRACIONES")
run_cmd("python manage.py makemigrations")
run_cmd("python manage.py migrate")

# Poblar datos
print("📝 ==> POBLAR DATOS")
run_cmd("python manage.py poblar_datos")

# Archivos estáticos
print("🎨 ==> ARCHIVOS ESTÁTICOS")
run_cmd("python manage.py collectstatic --noinput")

print("🎉 ==> SETUP COMPLETO")
print("🚀 ==> INICIANDO GUNICORN...")