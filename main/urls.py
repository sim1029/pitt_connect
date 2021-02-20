from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class/<int:class_id>/', views.class_page, name='class_page'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create, name='create'),
]
