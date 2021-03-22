from django.urls import path, include
from shop import views as v, views

urlpatterns = [
    path('', v.view_dishes, name='index'),
    path('', v.view_beverages, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
