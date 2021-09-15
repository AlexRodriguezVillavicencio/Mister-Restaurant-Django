from django.urls import path
from appRestaurant import views

urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('promociones',views.promociones, name="promociones"),
    path('menu/pollos-a-la-brasa',views.menupollo, name="menupollo"),
    path('menu/pollos-a-la-brasa/cuarto-pollo',views.menupollocuarto, name="menupollocuarto"),
]