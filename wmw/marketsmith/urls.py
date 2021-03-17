from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thegrowthlist', views.growth, name='growth'),
    path('industryrank', views.industryrank, name='industryrank'),
    path('the50', views.the50, name = 'the50'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout')
]