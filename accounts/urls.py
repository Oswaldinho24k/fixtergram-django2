from django.urls import path
from .views import ProfileView, RegistrationView, EditProfileView
from django.contrib.auth import views as logViews


app_name="accounts"

urlpatterns = [
	path('profile/', ProfileView.as_view(), name="profile"),
	path('register/', RegistrationView.as_view(), name="registro"),
	path('login/', logViews.login, name='login'),
	path('logout/', logViews.logout, name='logout'),
	path('edit/', EditProfileView.as_view(), name='edit'),
]