from django.urls import path
from . import views

app_name = 'tienda'

# Función de debug
def debug_view(request):
    from django.http import JsonResponse
    from django.db import connection
    
    try:
        # Verificar tablas en la base de datos
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [table[0] for table in cursor.fetchall()]
        
        # Intentar importar modelos
        from .models import Categoria, Producto
        
        info = {
            'database_tables': tables,
            'has_tienda_categoria': 'tienda_categoria' in tables,
            'has_tienda_producto': 'tienda_producto' in tables,
            'categorias_count': Categoria.objects.count() if 'tienda_categoria' in tables else 'N/A',
            'productos_count': Producto.objects.count() if 'tienda_producto' in tables else 'N/A',
            'status': 'OK' if 'tienda_categoria' in tables else 'MISSING_TABLES'
        }
        return JsonResponse(info)
    except Exception as e:
        import traceback
        return JsonResponse({
            'error': str(e),
            'traceback': traceback.format_exc(),
            'status': 'ERROR'
        }, status=500)

urlpatterns = [
    # Debug URL
    path('debug/', debug_view, name='debug'),
    
    # URLs principales
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/', views.productos, name='productos'),
    path('creditos/', views.creditos, name='creditos'),
    path('contacto/', views.contacto, name='contacto'),
    
    # URLs de productos
    path('editar-producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    # URLs de categorías
    path('editar-categoria/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('eliminar-categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
]