from django.shortcuts import render


def inicio(request):
    return render(request, "appRestaurant/index.html")

def promociones(request):
    return render(request, "appRestaurant/promociones.html")

def menupollo(request):
    return render(request, "appRestaurant/menupollo.html")

def menupollocuarto(request):
    return render(request, "appRestaurant/menupollocuarto.html")
