from django.urls import path
from . import views

urlpatterns = [
    path('view-cart/', views.view_cart, name="view_cart"),
    path('add/<str:id>/', views.add_to_cart, name="add_to_cart"),
    path('update/<str:id>/', views.adjust_cart, name="update_cart"),
    path('delete/<str:id>/', views.delete_item_from_cart, name="delete_item_from_cart"),
]