from unicodedata import name
from django.urls import path

from .views import *

urlpatterns = [
    path("login/", login_handler, name="login"),
    path("signup/", signup, name="signup"),
    path('logout/', logout_handler, name='logout'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name="delete_profile"),

    # api related paths
    path("sendcode/", send_code, name="send_code"),
    path("checkcode/", check_code, name="check_code"),
    path("checkusername/", check_username, name="check_username"),
    path("checkemail/", check_email, name="check_email"),
]
