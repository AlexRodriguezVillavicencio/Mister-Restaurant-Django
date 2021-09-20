from django.contrib import admin
from .models import Local, Direccion, Cliente, Pedido, Coordenada, Producto, Categoria, Promociones

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]


admin.site.register(Local)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Coordenada)
admin.site.register(Categoria)
admin.site.register(Promociones)
admin.site.register(Producto, ProductoAdmin)