from django.urls import path

from . import views

urlpatterns = [
	path('', views.hello),
	path('menu/', views.MenuList.as_view()),
]
