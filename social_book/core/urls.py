from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('like_post', views.like_post, name='like_post'),
    path('upload', views.upload, name='upload'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
