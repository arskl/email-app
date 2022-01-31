from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.main, name="main"),
    path('email-list/', views.email_list, name="list"),
]
