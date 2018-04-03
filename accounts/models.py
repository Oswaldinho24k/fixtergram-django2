from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	image = models.ImageField(upload_to='profile_img', blank=True, null=True)
	background = models.ImageField(upload_to='background_img', blank=True, null=True)
	birthday = models.DateField(auto_now_add=False, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	title = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user.username


