from django.urls import path
from . import views
from . views import StudentDeleteView, StudentUpdateView,\
	StudentListView, StudentCreateView

app_name = 'crudapp'

urlpatterns = [
	path('', StudentListView.as_view(), name='index'),
	#path('add_student/', views.add_student, name='add_student'),
	path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete'),
	path('<int:pk>/update/', StudentUpdateView.as_view(), name='update'),
	path('add_student/', StudentCreateView.as_view(), name='add_student'),
]