from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    """Modelo para las categorías de productos"""
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    icono = models.CharField(max_length=50, default="fas fa-tag", verbose_name="Icono FontAwesome")
    activa = models.BooleanField(default=True, verbose_name="Activa")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    """Modelo para los productos de la tienda"""
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='productos',
        verbose_name="Categoría"
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio"
    )
    precio_oferta = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio de Oferta"
    )
    imagen = models.ImageField(
        upload_to='productos/', 
        null=True, 
        blank=True,
        verbose_name="Imagen del Producto"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock Disponible")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    destacado = models.BooleanField(default=False, verbose_name="Producto Destacado")
    calificacion = models.DecimalField(
        max_digits=3, 
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],
        verbose_name="Calificación Promedio"
    )
    numero_resenas = models.PositiveIntegerField(default=0, verbose_name="Número de Reseñas")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.nombre
    
    @property
    def precio_final(self):
        """Devuelve el precio final (oferta si existe, sino precio normal)"""
        if self.precio_oferta and self.precio_oferta < self.precio:
            return self.precio_oferta
        return self.precio
    
    @property
    def tiene_descuento(self):
        """Verifica si el producto tiene descuento"""
        return bool(self.precio_oferta and self.precio_oferta < self.precio)
    
    @property
    def porcentaje_descuento(self):
        """Calcula el porcentaje de descuento"""
        if self.tiene_descuento:
            descuento = ((self.precio - self.precio_oferta) / self.precio) * 100
            return round(descuento, 0)
        return 0

class ImagenProducto(models.Model):
    """Modelo para imágenes adicionales de productos"""
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        related_name='imagenes_adicionales',
        verbose_name="Producto"
    )
    imagen = models.ImageField(upload_to='productos/adicionales/', verbose_name="Imagen")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="Texto Alternativo")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden de Visualización")
    
    class Meta:
        verbose_name = "Imagen Adicional"
        verbose_name_plural = "Imágenes Adicionales"
        ordering = ['orden']
    
    def __str__(self):
        return f"Imagen de {self.producto.nombre}"

class Resena(models.Model):
    """Modelo para reseñas de productos"""
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        related_name='resenas',
        verbose_name="Producto"
    )
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    email_cliente = models.EmailField(verbose_name="Email del Cliente")
    calificacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Calificación"
    )
    comentario = models.TextField(verbose_name="Comentario")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    aprobada = models.BooleanField(default=False, verbose_name="Reseña Aprobada")
    
    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ['-fecha_creacion']
        unique_together = ['producto', 'email_cliente']  # Un cliente, una reseña por producto
    
    def __str__(self):
        return f"Reseña de {self.nombre_cliente} para {self.producto.nombre}"
