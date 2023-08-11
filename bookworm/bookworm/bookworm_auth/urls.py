from django.urls import path

from bookworm.bookworm_auth.views import RegisterView, LoginUserView, LogoutUserView, register_view

urlpatterns = [
	path('register/', RegisterView.as_view(), name='register user'),
	path('login/', LoginUserView.as_view(), name='login user'),
	path('logout', LogoutUserView.as_view(), name='logout user'),

]
