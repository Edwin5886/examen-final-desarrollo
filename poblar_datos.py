"""
Script para poblar la base de datos con datos de ejemplo.
Ejecutar con: python manage.py shell < poblar_datos.py
"""

from tienda.models import Categoria, Producto
from django.utils import timezone
from decimal import Decimal

# Crear categorías
categorias_data = [
    {
        'nombre': 'Electrónicos',
        'descripcion': 'Dispositivos y gadgets modernos para tu vida digital',
        'icono': 'fas fa-laptop'
    },
    {
        'nombre': 'Ropa',
        'descripcion': 'Moda y vestimenta para toda la familia',
        'icono': 'fas fa-tshirt'
    },
    {
        'nombre': 'Hogar',
        'descripcion': 'Todo lo que necesitas para tu hogar',
        'icono': 'fas fa-home'
    },
    {
        'nombre': 'Deportes',
        'descripcion': 'Equipamiento y ropa deportiva',
        'icono': 'fas fa-football-ball'
    },
    {
        'nombre': 'Libros',
        'descripcion': 'Literatura, educación y entretenimiento',
        'icono': 'fas fa-book'
    },
]

print("Creando categorías...")
for cat_data in categorias_data:
    categoria, created = Categoria.objects.get_or_create(
        nombre=cat_data['nombre'],
        defaults={
            'descripcion': cat_data['descripcion'],
            'icono': cat_data['icono']
        }
    )
    if created:
        print(f"✓ Categoría '{categoria.nombre}' creada")
    else:
        print(f"- Categoría '{categoria.nombre}' ya existe")

# Obtener categorías para los productos
cat_electronicos = Categoria.objects.get(nombre='Electrónicos')
cat_ropa = Categoria.objects.get(nombre='Ropa')
cat_hogar = Categoria.objects.get(nombre='Hogar')
cat_deportes = Categoria.objects.get(nombre='Deportes')
cat_libros = Categoria.objects.get(nombre='Libros')

# Crear productos
productos_data = [
    # Electrónicos
    {
        'nombre': 'Samsung Galaxy S24',
        'descripcion': 'Smartphone de última generación con cámara de 200MP y pantalla AMOLED de 6.8 pulgadas',
        'categoria': cat_electronicos,
        'precio': Decimal('899.99'),
        'precio_oferta': Decimal('799.99'),
        'stock': 15,
        'destacado': True,
        'calificacion': Decimal('4.8')
    },
    {
        'nombre': 'MacBook Air M3',
        'descripcion': 'Laptop ultraligera con chip M3, perfecta para trabajo y creatividad',
        'categoria': cat_electronicos,
        'precio': Decimal('1299.99'),
        'stock': 8,
        'destacado': True,
        'calificacion': Decimal('4.9')
    },
    {
        'nombre': 'AirPods Pro 2da Gen',
        'descripcion': 'Auriculares inalámbricos con cancelación de ruido activa',
        'categoria': cat_electronicos,
        'precio': Decimal('249.99'),
        'precio_oferta': Decimal('199.99'),
        'stock': 25,
        'destacado': False,
        'calificacion': Decimal('4.7')
    },
    {
        'nombre': 'iPad Air 5ta Gen',
        'descripcion': 'Tablet versátil con chip M1 y pantalla Liquid Retina de 10.9 pulgadas',
        'categoria': cat_electronicos,
        'precio': Decimal('649.99'),
        'stock': 12,
        'destacado': True,
        'calificacion': Decimal('4.8')
    },
    
    # Ropa
    {
        'nombre': 'Chaqueta de Cuero Clásica',
        'descripcion': 'Chaqueta de cuero genuino, perfecta para cualquier ocasión',
        'categoria': cat_ropa,
        'precio': Decimal('199.99'),
        'precio_oferta': Decimal('149.99'),
        'stock': 20,
        'destacado': True,
        'calificacion': Decimal('4.6')
    },
    {
        'nombre': 'Jeans Premium Skinny',
        'descripcion': 'Jeans de alta calidad con corte moderno y cómodo',
        'categoria': cat_ropa,
        'precio': Decimal('89.99'),
        'stock': 30,
        'destacado': False,
        'calificacion': Decimal('4.4')
    },
    {
        'nombre': 'Vestido Elegante Negro',
        'descripcion': 'Vestido clásico negro, ideal para eventos especiales',
        'categoria': cat_ropa,
        'precio': Decimal('129.99'),
        'precio_oferta': Decimal('99.99'),
        'stock': 15,
        'destacado': True,
        'calificacion': Decimal('4.7')
    },
    
    # Hogar
    {
        'nombre': 'Robot Aspiradora Inteligente',
        'descripcion': 'Robot aspiradora con mapeo láser y control por app',
        'categoria': cat_hogar,
        'precio': Decimal('399.99'),
        'precio_oferta': Decimal('299.99'),
        'stock': 10,
        'destacado': True,
        'calificacion': Decimal('4.5')
    },
    {
        'nombre': 'Cafetera Espresso Profesional',
        'descripcion': 'Cafetera con molino integrado y espumador de leche',
        'categoria': cat_hogar,
        'precio': Decimal('599.99'),
        'stock': 6,
        'destacado': True,
        'calificacion': Decimal('4.8')
    },
    {
        'nombre': 'Lámpara LED Inteligente',
        'descripcion': 'Lámpara con control RGB y sincronización con música',
        'categoria': cat_hogar,
        'precio': Decimal('79.99'),
        'precio_oferta': Decimal('59.99'),
        'stock': 40,
        'destacado': False,
        'calificacion': Decimal('4.3')
    },
    
    # Deportes
    {
        'nombre': 'Bicicleta Montaña Pro',
        'descripcion': 'Bicicleta de montaña con suspensión completa y 21 velocidades',
        'categoria': cat_deportes,
        'precio': Decimal('899.99'),
        'precio_oferta': Decimal('749.99'),
        'stock': 5,
        'destacado': True,
        'calificacion': Decimal('4.9')
    },
    {
        'nombre': 'Zapatillas Running Elite',
        'descripcion': 'Zapatillas profesionales para running con tecnología de amortiguación',
        'categoria': cat_deportes,
        'precio': Decimal('159.99'),
        'stock': 25,
        'destacado': True,
        'calificacion': Decimal('4.6')
    },
    {
        'nombre': 'Pesas Ajustables 20kg',
        'descripcion': 'Set de pesas ajustables para entrenamiento en casa',
        'categoria': cat_deportes,
        'precio': Decimal('249.99'),
        'precio_oferta': Decimal('199.99'),
        'stock': 8,
        'destacado': False,
        'calificacion': Decimal('4.4')
    },
    
    # Libros
    {
        'nombre': 'Curso Completo de Python',
        'descripcion': 'Libro definitivo para aprender programación en Python desde cero',
        'categoria': cat_libros,
        'precio': Decimal('49.99'),
        'precio_oferta': Decimal('39.99'),
        'stock': 50,
        'destacado': True,
        'calificacion': Decimal('4.8')
    },
    {
        'nombre': 'El Arte de Cocinar',
        'descripcion': 'Libro de cocina con más de 200 recetas internacionales',
        'categoria': cat_libros,
        'precio': Decimal('34.99'),
        'stock': 30,
        'destacado': False,
        'calificacion': Decimal('4.5')
    },
    {
        'nombre': 'Mindset: La Nueva Psicología del Éxito',
        'descripcion': 'Libro de desarrollo personal y crecimiento profesional',
        'categoria': cat_libros,
        'precio': Decimal('24.99'),
        'precio_oferta': Decimal('19.99'),
        'stock': 35,
        'destacado': True,
        'calificacion': Decimal('4.7')
    },
]

print("\nCreando productos...")
productos_creados = 0
productos_existentes = 0

for prod_data in productos_data:
    producto, created = Producto.objects.get_or_create(
        nombre=prod_data['nombre'],
        defaults=prod_data
    )
    if created:
        productos_creados += 1
        print(f"✓ Producto '{producto.nombre}' creado - ${producto.precio}")
    else:
        productos_existentes += 1
        print(f"- Producto '{producto.nombre}' ya existe")

print(f"\n📊 Resumen:")
print(f"✓ Categorías: {Categoria.objects.count()}")
print(f"✓ Productos creados: {productos_creados}")
print(f"- Productos existentes: {productos_existentes}")
print(f"📦 Total productos: {Producto.objects.count()}")
print(f"⭐ Productos destacados: {Producto.objects.filter(destacado=True).count()}")
print(f"🏷️ Productos con oferta: {Producto.objects.exclude(precio_oferta__isnull=True).count()}")

print(f"\n🔐 Credenciales del admin:")
print(f"   Usuario: admin")
print(f"   Contraseña: admin123")
print(f"   URL Admin: http://127.0.0.1:8000/admin/")

print(f"\n🎉 ¡Base de datos poblada exitosamente!")