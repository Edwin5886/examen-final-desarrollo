import os
import sys
import django
from django.core.management import call_command

def setup_database():
    """Configura la base de datos para producción"""
    
    print("🔧 Configurando Django...")
    
    # Configurar Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final.settings')
    django.setup()
    
    print("🔧 Configurando base de datos...")
    
    # Ejecutar migraciones
    try:
        print("📦 Ejecutando migraciones...")
        call_command('migrate', verbosity=2)
        print("✅ Migraciones ejecutadas")
    except Exception as e:
        print(f"❌ Error en migraciones: {e}")
        return False
    
    # Importar modelos después de las migraciones
    try:
        from django.contrib.auth.models import User
        from tienda.models import Categoria, Producto
        
        # Crear superusuario
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@tienda.com', 'admin123')
            print("✅ Superusuario creado")
        else:
            print("✅ Superusuario ya existe")
        
        # Poblar datos
        if not Categoria.objects.exists():
            call_command('poblar_datos')
            print("✅ Datos poblados")
        else:
            print("✅ Datos ya existen")
            
    except Exception as e:
        print(f"❌ Error configurando datos: {e}")
        return False
    
    print("🎉 Setup completado exitosamente")
    return True

if __name__ == '__main__':
    setup_database()