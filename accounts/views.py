from django.shortcuts import render
from django.views.generic import View
from .models import Profile


class ProfileView(View):
	def get(self, request):
		queryset = Profile.objects.get(id=request.user.profile.id)
		template_name = 'profile.html'
		context = {
			'profile':queryset
		}

		return render(request, template_name, context)
