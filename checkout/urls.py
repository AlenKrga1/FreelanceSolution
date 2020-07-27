from django.urls import path
from . import views

urlpatterns = [
    path('', views.Checkout.as_view(), name="checkout"),
    # path('create-payment/', views.create_payment, name="create_payment")
]