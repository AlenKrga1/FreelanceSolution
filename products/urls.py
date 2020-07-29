from django.urls import path
from . import views


urlpatterns = [
	path('', views.products, name = 'products'),
	path('<int:id>/', views.view_product, name = 'view_product'),
	path('write-review/', views.WriteReview.as_view(), name = 'write-review'),
]