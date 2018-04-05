from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from .forms import UserRegistrationForm, ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from posts.models import Post



class ProfileView(View):
	@method_decorator(login_required)
	def get(self, request):
		queryset = Profile.objects.get(id=request.user.profile.id)
		#user_posts = Post.objects.all().filter(author=request.user)
		template_name = 'profile.html'
		context = {
			'profile':queryset,
		}

		return render(request, template_name, context)


class RegistrationView(View):

	def get(self, request):
		template_name= 'registration.html'
		form = UserRegistrationForm
		context = {
			'form': form 
		}
		return render(request, template_name, context)

	def post(self, request):
		template_name = 'registration.html'
		form = UserRegistrationForm(request.POST)
		context = {
			'form':form
		}
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			profile = Profile()
			profile.user = new_user
			profile.save()

			return redirect('accounts:login')
		else:
			return render(request, template_name, context)

class EditProfileView(View):
	@method_decorator(login_required)
	def get(self, request):
		queryset = Profile.objects.get(id=request.user.profile.id)
		template_name = 'edit_profile.html'
		form = ProfileForm(instance=queryset)
		context = {
			'form': form,
		
		}
		return render(request, template_name, context)

	def post(self, request):
		queryset = Profile.objects.get(id=request.user.profile.id)
		template_name = 'edit_profile.html'
		form = ProfileForm(request.POST, request.FILES, instance=queryset)

		context = {
		'form': form
		}

		if form.is_valid:
			form.save()
			return redirect('accounts:profile')













