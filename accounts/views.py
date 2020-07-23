from .forms import UserSignInForm, UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse

class SignIn(View):

	def get(self, request):
		form = UserSignInForm()

		return render(request, 'signin.html', {'form': form, 'next': request.GET.get('next', '')})

	def post(self, request):
		form = UserSignInForm(request.POST)

		if form.is_valid():
			user = auth.authenticate(
				form.cleaned_data['username_or_email'],
				password = form.cleaned_data['password']
			)

			if user:
				auth.login(request, user)
				print("successful")
				messages.info(request, "Sign in successful")

				if request.GET.get('next', '') != '':
					print("next")
					return redirect(request.GET.get('next'))
				else:
					print("index")
					return redirect(reverse('index'))
			else:
				form.add_error(None, "Your username or password are incorrect")

				return render(request, 'signin.html', {'form': form, 'next': request.GET.get('next', '')})
		else:
			form.add_error(None, "invalid Form")
			return render(request, 'signin.html', {'form': form, 'next': request.GET.get('next', '')})



class Register(View):

	def get(self, request):
		form = UserRegisterForm()

		return render(request, 'register.html', {'form': form, 'next': request.GET.get('next', '')})