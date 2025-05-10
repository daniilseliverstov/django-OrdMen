from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_user, name="login_page"),
    path("logout/", LogoutView.as_view(next_page="login_page"), name="logout"),
    path("profile/", views.profile_user, name="profile_page"),
]
