from django.urls import path
from . import views
from . views import StudentUpdateView, StudentDeleteView

app_name = 'crudapp'

urlpatterns = [
	path('', views.index, name='index'),
	path('add_student/', views.add_student, name='add_student'),
	path('<int:pk>/update/', StudentUpdateView.as_view(), name='update'),
	path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete'),
]