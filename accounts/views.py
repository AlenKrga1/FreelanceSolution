from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from .forms import UserSignInForm, UserRegisterForm, ContactMeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.mail import send_mail
from products.models import UserProduct
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse
from orders.models import Order


class ContactMe(View):

	def post(self, request):
		form = ContactMeForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			send_mail(
				f'You sent a message to Alen Krga',
				f'Thanks for reaching out! We will be in touch soon.\n\nMessage: "{message}"',
				'alen.krga1@gmail.com',
				[email],
				fail_silently=True,
			)

			send_mail(
				f'You have a new message from {email}',
				f'Message: {message}',
				'alen.krga1@gmail.com',
				['alen.krga1@gmail.com'],
				fail_silently=True,
			)

			messages.info(request, "Message sent!")
			return redirect(reverse('index'))

		messages.error(request, "Invalid form")
		return redirect(reverse('contact-me'))


	def get(self, request):
		form = ContactMeForm()

		return render(request, 'contact_me.html', {'form': form})


@login_required
def profile(request):
	user_products = UserProduct.objects.filter(user = request.user)
	orders = Order.objects.filter(user = request.user)

	return render(request, 'profile.html', {'user_products': user_products, 'orders': orders})

@login_required
def logout(request):
	auth.logout(request)

	return redirect(reverse('index'))

class SignIn(UserPassesTestMixin, AccessMixin, View):

	def test_func(self):
		return self.request.user.is_anonymous

	def handle_no_permission(self):
		return redirect(reverse('profile'))

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
				# messages.success(request, "Sign in successful")

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



class Register(UserPassesTestMixin, AccessMixin, View):

	def test_func(self):
		return self.request.user.is_anonymous

	def handle_no_permission(self):
		return redirect(reverse('profile'))

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

				# messages.success(request, "You have successfully registered")

				return redirect(reverse('index'))

			else:
				form.add_error(None, "Your username or password are incorrect")

				return render(request, 'register.html', {'form': form, 'next': request.GET.get('next', '')})

		else:
			form.add_error(None, "invalid Form")
			
			return render(request, 'register.html', {'form': form, 'next': request.GET.get('next', '')})