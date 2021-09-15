from django.contrib import admin
from .models import Local, Direccion, Cliente, Pedido, Coordenada, Producto

admin.site.register(Local)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Coordenada)