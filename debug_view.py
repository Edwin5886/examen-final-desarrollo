from django.shortcuts import render
from django.http import JsonResponse
import traceback
import sys

def debug_view(request):
    """Vista de debug para diagnosticar problemas"""
    try:
        # Importar modelos
        from tienda.models import Categoria, Producto
        
        diagnostico = {
            'python_version': sys.version,
            'categorias_count': Categoria.objects.count(),
            'productos_count': Producto.objects.count(),
            'database_ok': True
        }
        
        # Intentar obtener una categoría
        try:
            primera_categoria = Categoria.objects.first()
            diagnostico['primera_categoria'] = primera_categoria.nombre if primera_categoria else "No hay categorías"
        except Exception as e:
            diagnostico['categoria_error'] = str(e)
        
        return JsonResponse(diagnostico)
        
    except Exception as e:
        error_info = {
            'error': str(e),
            'error_type': type(e).__name__,
            'traceback': traceback.format_exc(),
            'database_ok': False
        }
        return JsonResponse(error_info, status=500)