from django.db import  models
# from django.db.models.deletion import CASCADE

# Create your models here.
class Local(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)

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





class Cliente(models.Model):
    DNI = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    celular = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Datos del cliente'
        verbose_name_plural = 'Datos de los clientes'
    
    def __str__(self):
        return self.nombre



class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

class Producto(models.Model):
    ID_cod = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField (max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    descripcion = models.CharField('Breve descripción del producto',max_length=255, blank=True,null=True)
    contenido = models.CharField('Contenido del producto',max_length=255)
    imagen = models.ImageField(upload_to='img',blank=True,null=True)
    extra = models.FileField(upload_to='assets',blank=True,null=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

class Coordenada(models.Model):
    latitud = models.DecimalField(max_digits=12, decimal_places=10)
    longitud = models.DecimalField(max_digits=13, decimal_places=10)

class Pedido(models.Model):
     cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
     fecha = models.DateField(auto_now_add=True)
     descripcion = models.CharField('Productos que contiene el Pedido', max_length=255)
     detalles = models.CharField('Gustos del cliente',max_length=255)
     local = models.ForeignKey(Local, on_delete=models.RESTRICT)
     direccion = models.OneToOneField(Direccion, on_delete=models.RESTRICT)
     coordenada = models.OneToOneField(Coordenada , on_delete=models.RESTRICT)

    

