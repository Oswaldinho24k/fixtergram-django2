from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Post(models.Model):

	author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(max_length=280)
	tags = models.ManyToManyField(Tag, related_name='posts')
	image = models.ImageField(upload_to='posts')
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

