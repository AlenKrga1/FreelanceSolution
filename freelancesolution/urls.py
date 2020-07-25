"""freelancesolution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from products.views import Products, view_product
import accounts.views as accounts
from django.conf import settings
from django.contrib import admin
from home.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('products/', Products.as_view(), name = 'products'),
    path('product/<int:id>/', view_product, name = 'view_product'),
    path('sign-in/', accounts.SignIn.as_view(), name = 'sign-in'),
    path('register/', accounts.Register.as_view(), name = 'register'),
    path('logout/', accounts.logout, name = 'logout'),
    path('cart/', include("cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
