from django.core.management.base import BaseCommand
from tienda.models import Categoria, Producto
from decimal import Decimal

class Command(BaseCommand):
    help = 'Poblar la base de datos con datos de ejemplo'

    def handle(self, *args, **options):
        self.stdout.write("Poblando base de datos con datos de ejemplo...")

        # Crear categorías
        categorias_data = [
            {
                'nombre': 'Electronicos',
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
                'descripcion': 'Literatura, educacion y entretenimiento',
                'icono': 'fas fa-book'
            },
        ]

        self.stdout.write("Creando categorias...")
        for cat_data in categorias_data:
            categoria, created = Categoria.objects.get_or_create(
                nombre=cat_data['nombre'],
                defaults={
                    'descripcion': cat_data['descripcion'],
                    'icono': cat_data['icono']
                }
            )
            if created:
                self.stdout.write(f"✓ Categoria '{categoria.nombre}' creada")
            else:
                self.stdout.write(f"- Categoria '{categoria.nombre}' ya existe")

        # Obtener categorías para los productos
        cat_electronicos = Categoria.objects.get(nombre='Electronicos')
        cat_ropa = Categoria.objects.get(nombre='Ropa')
        cat_hogar = Categoria.objects.get(nombre='Hogar')
        cat_deportes = Categoria.objects.get(nombre='Deportes')
        cat_libros = Categoria.objects.get(nombre='Libros')

        # Crear productos
        productos_data = [
            # Electronicos
            {
                'nombre': 'Samsung Galaxy S24',
                'descripcion': 'Smartphone de ultima generacion con camara de 200MP y pantalla AMOLED de 6.8 pulgadas',
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
                'descripcion': 'Auriculares inalambricos con cancelacion de ruido activa',
                'categoria': cat_electronicos,
                'precio': Decimal('249.99'),
                'precio_oferta': Decimal('199.99'),
                'stock': 25,
                'destacado': False,
                'calificacion': Decimal('4.7')
            },
            {
                'nombre': 'iPad Air 5ta Gen',
                'descripcion': 'Tablet versatil con chip M1 y pantalla Liquid Retina de 10.9 pulgadas',
                'categoria': cat_electronicos,
                'precio': Decimal('649.99'),
                'stock': 12,
                'destacado': True,
                'calificacion': Decimal('4.8')
            },
            
            # Ropa
            {
                'nombre': 'Chaqueta de Cuero Clasica',
                'descripcion': 'Chaqueta de cuero genuino, perfecta para cualquier ocasion',
                'categoria': cat_ropa,
                'precio': Decimal('199.99'),
                'precio_oferta': Decimal('149.99'),
                'stock': 20,
                'destacado': True,
                'calificacion': Decimal('4.6')
            },
            {
                'nombre': 'Jeans Premium Skinny',
                'descripcion': 'Jeans de alta calidad con corte moderno y comodo',
                'categoria': cat_ropa,
                'precio': Decimal('89.99'),
                'stock': 30,
                'destacado': False,
                'calificacion': Decimal('4.4')
            },
            {
                'nombre': 'Vestido Elegante Negro',
                'descripcion': 'Vestido clasico negro, ideal para eventos especiales',
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
                'descripcion': 'Robot aspiradora con mapeo laser y control por app',
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
                'nombre': 'Lampara LED Inteligente',
                'descripcion': 'Lampara con control RGB y sincronizacion con musica',
                'categoria': cat_hogar,
                'precio': Decimal('79.99'),
                'precio_oferta': Decimal('59.99'),
                'stock': 40,
                'destacado': False,
                'calificacion': Decimal('4.3')
            },
            
            # Deportes
            {
                'nombre': 'Bicicleta Montana Pro',
                'descripcion': 'Bicicleta de montana con suspension completa y 21 velocidades',
                'categoria': cat_deportes,
                'precio': Decimal('899.99'),
                'precio_oferta': Decimal('749.99'),
                'stock': 5,
                'destacado': True,
                'calificacion': Decimal('4.9')
            },
            {
                'nombre': 'Zapatillas Running Elite',
                'descripcion': 'Zapatillas profesionales para running con tecnologia de amortiguacion',
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
                'descripcion': 'Libro definitivo para aprender programacion en Python desde cero',
                'categoria': cat_libros,
                'precio': Decimal('49.99'),
                'precio_oferta': Decimal('39.99'),
                'stock': 50,
                'destacado': True,
                'calificacion': Decimal('4.8')
            },
            {
                'nombre': 'El Arte de Cocinar',
                'descripcion': 'Libro de cocina con mas de 200 recetas internacionales',
                'categoria': cat_libros,
                'precio': Decimal('34.99'),
                'stock': 30,
                'destacado': False,
                'calificacion': Decimal('4.5')
            },
            {
                'nombre': 'Mindset: La Nueva Psicologia del Exito',
                'descripcion': 'Libro de desarrollo personal y crecimiento profesional',
                'categoria': cat_libros,
                'precio': Decimal('24.99'),
                'precio_oferta': Decimal('19.99'),
                'stock': 35,
                'destacado': True,
                'calificacion': Decimal('4.7')
            },
        ]

        self.stdout.write("\nCreando productos...")
        productos_creados = 0
        productos_existentes = 0

        for prod_data in productos_data:
            producto, created = Producto.objects.get_or_create(
                nombre=prod_data['nombre'],
                defaults=prod_data
            )
            if created:
                productos_creados += 1
                self.stdout.write(f"✓ Producto '{producto.nombre}' creado - ${producto.precio}")
            else:
                productos_existentes += 1
                self.stdout.write(f"- Producto '{producto.nombre}' ya existe")

        self.stdout.write(f"\n📊 Resumen:")
        self.stdout.write(f"✓ Categorias: {Categoria.objects.count()}")
        self.stdout.write(f"✓ Productos creados: {productos_creados}")
        self.stdout.write(f"- Productos existentes: {productos_existentes}")
        self.stdout.write(f"📦 Total productos: {Producto.objects.count()}")
        self.stdout.write(f"⭐ Productos destacados: {Producto.objects.filter(destacado=True).count()}")
        self.stdout.write(f"🏷️ Productos con oferta: {Producto.objects.exclude(precio_oferta__isnull=True).count()}")

        self.stdout.write(self.style.SUCCESS(f"\n🎉 ¡Base de datos poblada exitosamente!"))
        self.stdout.write(f"\n🔐 Credenciales del admin:")
        self.stdout.write(f"   Usuario: admin")
        self.stdout.write(f"   Contraseña: admin123")
        self.stdout.write(f"   URL Admin: http://127.0.0.1:8000/admin/")