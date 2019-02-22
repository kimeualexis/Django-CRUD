from django.urls import path
from . import views

app_name = 'crudapp'

urlpatterns = [
	path('', views.index, name='index'),
	path('add_student/', views.add_student, name='add_student'),
]