from django.urls import path

from .views import *

urlpatterns = [

    path('', home, name="home"),

    path('post/', create_post, name='post'),
    path('post/<int:id>/edit/', edit_post, name='edit_post'),
    path('post/<int:id>/delete/', delete_post, name='delete_post'),
    path('post/<int:id>', post_detail, name='post_detail'),

    path('sendrequest/<int:post1>/<int:post2>/', send_request, name='send_request'),

    path('edit/', edit_profile, name='edit_profile'),
    path('<username>/', others_profile, name="others_profile"),
]
