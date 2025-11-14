from django.contrib import admin
from django.db import models
from .models import Categoria, Producto, ImagenProducto, Resena

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'fecha_creacion']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['activa']
    ordering = ['nombre']

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1
    fields = ['imagen', 'alt_text', 'orden']

class ResenaInline(admin.TabularInline):
    model = Resena
    extra = 0
    readonly_fields = ['fecha_creacion']
    fields = ['nombre_cliente', 'calificacion', 'comentario', 'aprobada', 'fecha_creacion']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'categoria', 'precio', 'precio_oferta', 
        'stock', 'disponible', 'destacado', 'calificacion'
    ]
    list_filter = [
        'categoria', 'disponible', 'destacado', 
        'fecha_creacion', 'fecha_actualizacion'
    ]
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'precio_oferta', 'stock', 'disponible', 'destacado']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    inlines = [ImagenProductoInline, ResenaInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'categoria')
        }),
        ('Precios e Inventario', {
            'fields': ('precio', 'precio_oferta', 'stock', 'disponible')
        }),
        ('Configuración', {
            'fields': ('imagen', 'destacado')
        }),
        ('Calificaciones', {
            'fields': ('calificacion', 'numero_resenas'),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Actualizar número de reseñas automáticamente
        super().save_model(request, obj, form, change)
        obj.numero_resenas = obj.resenas.filter(aprobada=True).count()
        if obj.numero_resenas > 0:
            calificacion_promedio = obj.resenas.filter(aprobada=True).aggregate(
                promedio=models.Avg('calificacion')
            )['promedio']
            obj.calificacion = round(calificacion_promedio, 2)
        obj.save()

@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'alt_text', 'orden']
    list_filter = ['producto__categoria']
    search_fields = ['producto__nombre', 'alt_text']
    ordering = ['producto', 'orden']

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = [
        'producto', 'nombre_cliente', 'calificacion', 
        'fecha_creacion', 'aprobada'
    ]
    list_filter = ['calificacion', 'aprobada', 'fecha_creacion', 'producto__categoria']
    search_fields = ['producto__nombre', 'nombre_cliente', 'comentario']
    list_editable = ['aprobada']
    readonly_fields = ['fecha_creacion']
    ordering = ['-fecha_creacion']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Actualizar calificación del producto
        producto = obj.producto
        resenas_aprobadas = producto.resenas.filter(aprobada=True)
        producto.numero_resenas = resenas_aprobadas.count()
        if producto.numero_resenas > 0:
            from django.db.models import Avg
            calificacion_promedio = resenas_aprobadas.aggregate(
                promedio=Avg('calificacion')
            )['promedio']
            producto.calificacion = round(calificacion_promedio, 2)
        producto.save()

# Personalizar el título del admin
admin.site.site_header = "Administración de Mi Tienda"
admin.site.site_title = "Mi Tienda Admin"
admin.site.index_title = "Panel de Administración"
