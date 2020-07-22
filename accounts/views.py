from .forms import UserSignInForm, UserRegisterForm
from django.views.generic import View
from django.shortcuts import render

class SignIn(View):

	def get(self, request):
		form = UserSignInForm()

		return render(request, 'signin.html', {'form': form, 'next': request.GET.get('next', '')})



class Register(View):

	def get(self, request):
		form = UserRegisterForm()

		return render(request, 'register.html', {'form': form, 'next': request.GET.get('next', '')})