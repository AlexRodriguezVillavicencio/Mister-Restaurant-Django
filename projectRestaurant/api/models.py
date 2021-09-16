from django.db import  models

# Create your models here.
class Local(models.Model):
    ID_local = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=12, decimal_places=10)
    longitud = models.DecimalField(max_digits=13, decimal_places=10)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    nro_pedido = models.BigAutoField(primary_key=True)
    ciudad = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    zona = models.CharField('Dirección',max_length=100)
    referencia = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Dirección del cliente Delivery'
        verbose_name_plural = 'Dirección del cliente Delivery'

    def __str__(self):
        return f'{self.distrito} {self.zona}'


class Coordenada(models.Model):
    nro_pedido = models.BigAutoField(primary_key=True)
    latitud = models.DecimalField(max_digits=12, decimal_places=10)
    longitud = models.DecimalField(max_digits=13, decimal_places=10)

    class Meta:
        verbose_name = 'Coordenada del cliente Delivery'
        verbose_name_plural = 'Coordenada del cliente Delivery'


class Cliente(models.Model):
    nro_cliente = models.BigAutoField(primary_key=True)
    DNI = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(max_length=254)
    direccion_ID = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    coordenada_ID = models.ForeignKey(Coordenada, on_delete=models.CASCADE)
    local_ID = models.ForeignKey(Local, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Datos del cliente'
        verbose_name_plural = 'Datos de los clientes'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    ID_cod = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField (max_digits=6, decimal_places=2)
    descuento = models.DecimalField(max_digits=4, decimal_places=2)
    descripcion = models.TextField('Breve descripción del producto')
    contenido = models.CharField('Contenido del producto',max_length=255)
    imagen = models.ImageField
    extra = models.FileField
    cliente_ID = models.ManyToManyField(Cliente)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
     nro_pedido = models.BigAutoField(primary_key=True)
     fecha_hora = models.DateField
     descripcion = models.CharField('Productos que contiene el Pedido', max_length=255)
     detalles = models.CharField('Gustos del cliente',max_length=255)
     producto_ID = models.ManyToManyField(Producto)
     direccion_ID = models.ForeignKey(Direccion, on_delete=models.CASCADE)
     coordenada_ID = models.ForeignKey(Coordenada, on_delete=models.CASCADE)
     local_ID = models.OneToOneField(Local, on_delete=models.CASCADE)
