from django.shortcuts import render
from api.models import Producto
# from django.conf import settings

def inicio(request):
    return render(request, "appRestaurant/index.html")

def promociones(request):
    return render(request, "appRestaurant/promociones.html")

def menupollo(request):
    producto = Producto.objects.all()
    #equivalente a : select * from producto where id = producto_id
    return render(request, "appRestaurant/menupollo.html",{'producto':producto})

def menupollocuarto(request):
    return render(request, "appRestaurant/menupollocuarto.html")
