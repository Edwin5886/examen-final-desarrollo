import os
import sys

# Agregar el directorio del proyecto al path
sys.path.append('/app')

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')

import django
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User
from tienda.models import Categoria, Producto

def setup_database():
    """Configura la base de datos para producción"""
    
    print("🔧 Configurando base de datos...")
    
    # Ejecutar migraciones
    try:
        call_command('migrate', verbosity=0)
        print("✅ Migraciones ejecutadas")
    except Exception as e:
        print(f"❌ Error en migraciones: {e}")
    
    # Crear superusuario
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@tienda.com', 'admin123')
            print("✅ Superusuario creado")
        else:
            print("✅ Superusuario ya existe")
    except Exception as e:
        print(f"❌ Error creando superusuario: {e}")
    
    # Poblar datos
    try:
        if not Categoria.objects.exists():
            call_command('poblar_datos')
            print("✅ Datos poblados")
        else:
            print("✅ Datos ya existen")
    except Exception as e:
        print(f"❌ Error poblando datos: {e}")
    
    print("🎉 Setup completado")

if __name__ == '__main__':
    setup_database()