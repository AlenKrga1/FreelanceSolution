from django.urls import path
from . import views


urlpatterns = [
	path('custom-design/', views.CustomDesign.as_view(), name = 'custom_design'),
]