from . import views
from django.urls import path

urlpatterns = [
    path('members/', views.members, name='members'),
    path('products/', views.products, name="products")
]