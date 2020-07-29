from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
	path('sign-in/', views.SignIn.as_view(), name = 'sign-in'),
	path('register/', views.Register.as_view(), name = 'register'),
	path('logout/', views.logout, name = 'logout'),
	path('profile/', views.profile, name='profile'),
	path('contact-me/', views.ContactMe.as_view(), name='contact-me'),
	path('password-reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
	path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path("<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
	path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]