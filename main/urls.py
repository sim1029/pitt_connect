from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class/<int:class_id>/', views.class_page, name='class_page'),
]
