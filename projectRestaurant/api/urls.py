from django.urls import path
# from django.urls.resolvers import URLPattern
from api.api import local_api_view

urlpatterns = [
    path('', local_api_view, name="api_local")
]