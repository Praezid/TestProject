from products import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('products/<int:pk>', views.products_pk),
    path('products/count', views.count),
    path('products/expensivest', views.expensivest),
    path('products/cheapest', views.cheapest),
    path('products/median', views.median),
]
