from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('contents/', views.content_list, name='content_list'),
    path('contents/create/', views.content_create, name='content_create'),
    path('inspect/', views.model_inspection, name='model_inspection'),
]