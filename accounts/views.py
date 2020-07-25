from django.contrib.auth.decorators import login_required
from .forms import UserSignInForm, UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from products.models import UserProduct
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse


@login_required
def profile(request):
	user_products = UserProduct.objects.filter(user = request.user)

	return render(request, 'profile.html', {'user_products': user_products})

@login_required
def logout(request):
	auth.logout(request)

	return redirect(reverse('index'))

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
				messages.success(request, "Sign in successful")

				if request.GET.get('next', '') != '':
					return redirect(request.GET.get('next'))
				else:
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


	def post(self, request):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()

			user = auth.authenticate(
				form.cleaned_data['username'],
				password = form.cleaned_data['password1']
			)

			if user:
				auth.login(request, user)

				messages.success(request, "You have successfully registered")

				return redirect(reverse('index'))

			else:
				form.add_error(None, "Your username or password are incorrect")

				return render(request, 'register.html', {'form': form, 'next': request.GET.get('next', '')})

		else:
			form.add_error(None, "invalid Form")
			
			return render(request, 'register.html', {'form': form, 'next': request.GET.get('next', '')})