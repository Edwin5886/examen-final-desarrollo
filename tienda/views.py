from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
