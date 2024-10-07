from django.contrib import admin
from django.urls import path
from home.views import post_list, like_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('admin/', admin.site.urls),
]