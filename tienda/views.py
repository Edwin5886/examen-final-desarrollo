from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
import os
from .models import Categoria, Producto, Resena
from .forms import ProductoForm, CategoriaForm

def inicio(request):
    """Vista para la página de inicio"""
    productos_destacados = Producto.objects.filter(
        destacado=True, 
        disponible=True
    ).select_related('categoria')[:6]
    
    context = {
        'titulo': 'Bienvenido a Nuestra Tienda',
        'mensaje': 'Encuentra los mejores productos para tu estilo de vida',
        'productos_destacados': productos_destacados
    }
    return render(request, 'tienda/inicio.html', context)

def categorias(request):
    """Vista para la página de categorías"""
    categorias_lista = Categoria.objects.filter(activa=True).prefetch_related('productos')
    
    context = {
        'titulo': 'Categorías',
        'categorias': categorias_lista
    }
    return render(request, 'tienda/categorias.html', context)

def productos(request):
    """Vista para la página de productos con opción de agregar"""
    from django.http import HttpResponse
    
    try:
        # Verificar que las tablas existan
        from .models import Categoria, Producto
        
        # Manejar formulario de agregar producto
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                producto = form.save()
                messages.success(request, f'Producto "{producto.nombre}" agregado exitosamente.')
                return redirect('tienda:productos')
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario.')
        else:
            form = ProductoForm()
        
        # Obtener todos los productos
        productos_lista = Producto.objects.all().select_related('categoria').order_by('-fecha_creacion')
        
        context = {
            'titulo': 'Productos',
            'productos': productos_lista,
            'form': form
        }
        return render(request, 'tienda/productos.html', context)
        
    except Exception as e:
        # Si las tablas no existen o hay otro error
        error_msg = f"""
        <h1>Error en la página de productos</h1>
        <p><strong>Error:</strong> {str(e)}</p>
        <p><strong>Solución:</strong> Las migraciones de base de datos no se ejecutaron correctamente.</p>
        <p><a href="/admin/">Ir al Admin</a> | <a href="/">Volver al Inicio</a></p>
        <hr>
        <p><em>Railway está configurando la base de datos. Espera 1-2 minutos y recarga la página.</em></p>
        """
        return HttpResponse(error_msg)

def editar_producto(request, producto_id):
    """Vista para editar un producto"""
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado exitosamente.')
            return redirect('tienda:productos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm(instance=producto)
    
    context = {
        'titulo': f'Editar: {producto.nombre}',
        'form': form,
        'producto': producto,
        'editando': True
    }
    return render(request, 'tienda/editar_producto.html', context)

def eliminar_producto(request, producto_id):
    """Vista para eliminar un producto"""
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado exitosamente.')
        return redirect('tienda:productos')
    
    return redirect('tienda:productos')

def creditos(request):
    """Vista para la página de créditos"""
    context = {
        'titulo': 'Créditos',
        'desarrollador': 'Edwin',
        'fecha_creacion': '2025',
        'descripcion': 'Sitio web desarrollado como proyecto de emprendimiento con Django y MySQL'
    }
    return render(request, 'tienda/creditos.html', context)

def contacto(request):
    """Vista para la página de contacto"""
    context = {
        'titulo': 'Contáctanos',
        'email': 'info@mitienda.com',
        'telefono': '+1 234 567 8900',
        'direccion': 'Calle Principal #123, Ciudad'
    }
    return render(request, 'tienda/contacto.html', context)

# ========== VISTAS PARA CATEGORÍAS ==========

def categorias(request):
    """Vista para listar y agregar categorías"""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, f'Categoría "{categoria.nombre}" creada exitosamente.')
            return redirect('tienda:categorias')
        else:
            messages.error(request, 'Error al crear la categoría. Revisa los datos.')
    else:
        form = CategoriaForm()
    
    categorias_list = Categoria.objects.all().order_by('-fecha_creacion')
    
    context = {
        'titulo': 'Gestión de Categorías',
        'categorias': categorias_list,
        'form': form,
        'total_categorias': categorias_list.count(),
        'categorias_activas': categorias_list.filter(activa=True).count(),
    }
    return render(request, 'tienda/categorias.html', context)

def editar_categoria(request, categoria_id):
    """Vista para editar una categoría específica"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, f'Categoría "{categoria.nombre}" actualizada exitosamente.')
            return redirect('tienda:categorias')
        else:
            messages.error(request, 'Error al actualizar la categoría. Revisa los datos.')
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {
        'titulo': 'Editar Categoría',
        'categoria': categoria,
        'form': form,
    }
    return render(request, 'tienda/editar_categoria.html', context)

def eliminar_categoria(request, categoria_id):
    """Vista para eliminar una categoría"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    # Verificar si la categoría tiene productos asociados
    productos_asociados = Producto.objects.filter(categoria=categoria).count()
    
    if productos_asociados > 0:
        messages.warning(
            request, 
            f'No se puede eliminar la categoría "{categoria.nombre}" porque tiene {productos_asociados} producto(s) asociado(s).'
        )
    else:
        nombre_categoria = categoria.nombre
        categoria.delete()
        messages.success(request, f'Categoría "{nombre_categoria}" eliminada exitosamente.')
    
    return redirect('tienda:categorias')

def railway_debug(request):
    """Vista de diagnóstico para Railway"""
    env_vars = {}
    
    # Variables de Railway importantes
    railway_vars = [
        'RAILWAY_ENVIRONMENT_NAME', 'DATABASE_URL', 'DATABASE_PRIVATE_URL',
        'PGDATABASE', 'PGUSER', 'PGPASSWORD', 'PGHOST', 'PGPORT',
        'POSTGRES_URL', 'POSTGRES_PRIVATE_URL'
    ]
    
    for var in railway_vars:
        value = os.environ.get(var)
        if value:
            # Ocultar contraseñas para seguridad
            if 'PASSWORD' in var or 'URL' in var:
                env_vars[var] = value[:20] + '...' if len(value) > 20 else 'SET'
            else:
                env_vars[var] = value
        else:
            env_vars[var] = 'NO_SET'
    
    # Info de la base de datos actual
    db_config = settings.DATABASES['default']
    
    # Intentar contar categorías
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM tienda_categoria")
            categoria_count = cursor.fetchone()[0]
        db_status = f"OK - {categoria_count} categorías"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"
    
    debug_info = {
        'environment_variables': env_vars,
        'database_config': {
            'engine': db_config['ENGINE'],
            'name': str(db_config.get('NAME', 'N/A')),  # Convertir PosixPath a string
            'host': str(db_config.get('HOST', 'N/A')),
            'port': str(db_config.get('PORT', 'N/A')),
        },
        'database_status': db_status,
        'is_railway': bool(os.environ.get('RAILWAY_ENVIRONMENT_NAME')),
    }
    
    return JsonResponse(debug_info, json_dumps_params={'indent': 2})

def railway_init(request):
    """Vista para forzar inicialización de Railway"""
    import subprocess
    
    results = []
    
    def run_init_cmd(cmd, description):
        try:
            results.append(f"🚀 {description}")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                results.append(f"✅ {description} - EXITOSO")
                if result.stdout:
                    results.append(f"📤 {result.stdout[:200]}")
            else:
                results.append(f"❌ {description} - ERROR")
                if result.stderr:
                    results.append(f"⚠️ {result.stderr[:200]}")
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            results.append(f"⏱️ {description} - TIMEOUT")
            return False
        except Exception as e:
            results.append(f"💥 {description} - EXCEPCIÓN: {str(e)}")
            return False
    
    # Ejecutar inicialización
    results.append("🔧 INICIANDO CONFIGURACIÓN MANUAL DE RAILWAY")
    
    run_init_cmd("python manage.py makemigrations", "Crear migraciones")
    run_init_cmd("python manage.py migrate", "Ejecutar migraciones")
    run_init_cmd("python manage.py poblar_datos", "Poblar datos")
    
    # Verificar resultado
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM tienda_categoria")
            count = cursor.fetchone()[0]
        results.append(f"🎉 INICIALIZACIÓN COMPLETA - {count} categorías creadas")
        status = "SUCCESS"
    except Exception as e:
        results.append(f"❌ VERIFICACIÓN FALLÓ: {str(e)}")
        status = "FAILED"
    
    return JsonResponse({
        "status": status,
        "log": results,
        "next_step": "Ahora puedes acceder a /productos/ y /categorias/"
    }, json_dumps_params={'indent': 2})
