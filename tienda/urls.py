from django.urls import path
from . import views

app_name = 'tienda'

# Función de debug
def debug_view(request):
    from django.http import JsonResponse
    from .models import Categoria, Producto
    try:
        info = {
            'categorias': Categoria.objects.count(),
            'productos': Producto.objects.count(),
            'status': 'OK'
        }
        return JsonResponse(info)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

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