from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import NewPostForm

# Create your views here.
class PostListView(View):
	def get(self, request):
		template_name='posts.html'
		queryset = Post.objects.all()
		context = {
			'posts': queryset
		}
		return render(request, template_name, context)

class NewPost(View):
	def get(self, request):
		template_name = 'new_post.html'
		form = NewPostForm
		context = {
			'form': form
		}
		return render(request, template_name, context)

	def post(self, request):
		form = NewPostForm(request.POST, request.FILES)
		context = {
			'form': form
		}
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()

		return redirect('posts:list')

