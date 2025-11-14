#!/usr/bin/env python
import os
import subprocess

def run_cmd(cmd):
    print(f"🚀 Ejecutando: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True)
    if result.returncode == 0:
        print(f"✅ Completado: {cmd}")
    else:
        print(f"❌ Error en: {cmd}")
    return result.returncode == 0

print("🔧 ==> INICIANDO RAILWAY SETUP")

# Configurar entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')

# Migraciones
print("📦 ==> MIGRACIONES")
run_cmd("python manage.py makemigrations --noinput")
run_cmd("python manage.py migrate --noinput")

# Poblar datos
print("📝 ==> POBLAR DATOS")
run_cmd("python manage.py poblar_datos")

print("🎉 ==> SETUP COMPLETO")
print("🚀 ==> INICIANDO GUNICORN...")