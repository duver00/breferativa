from django.urls import path, re_path
from core.views import InventarioList, buscar_inventario


urlpatterns = [
    path('', InventarioList.as_view(), name='home'),
    re_path(r'^results/$', buscar_inventario, name='results'),
]
