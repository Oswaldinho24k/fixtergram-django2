from django.urls import path
from .views import PostListView, NewPost


app_name="posts"
urlpatterns = [
	path('', PostListView.as_view(), name='list'),
	path('new/', NewPost.as_view(), name='new')
]