from django.shortcuts import render
from api.models import Producto, Promociones


def inicio(request):
    return render(request, "appRestaurant/index.html")

def promociones(request):
    promociones = Promociones.objects.all()
    return render(request, "appRestaurant/promociones.html", {'promociones':promociones})

def menupollo(request):
    producto = Producto.objects.all()
    #equivalente a : select * from producto where id = producto_id
    return render(request, "appRestaurant/menupollo.html",{'producto':producto})

def menupollocuarto(request):
    producto = Producto.objects.all()
    return render(request, "appRestaurant/menupollocuarto.html", {'producto':producto})
