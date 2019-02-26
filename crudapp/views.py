from django.shortcuts import render, reverse, redirect
from . models import Student
from . forms import StudentForm
from django.views.generic import DeleteView,\
	UpdateView, ListView, CreateView


# Create your views here.
class StudentListView(ListView):
	model = Student
	template_name = 'crudapp/index.html'
	context_object_name = 'students'

"""
def add_student(request):
	form = StudentForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		student = form.save(commit=False)
		student.passport = request.FILES['passport']
		student.save()
		students = Student.objects.all()
		return render(request, 'crudapp/index.html', {'students': students})
	return render(request, 'crudapp/add_student.html', {'form': form})
"""


class StudentCreateView(CreateView):
	model = Student
	fields = ['firstname', 'lastname', 'adm_no', 'passport']
	template_name = 'crudapp/add_student.html'


class StudentDeleteView(DeleteView):
	model = Student
	success_url = '/'


class StudentUpdateView(UpdateView):
	model = Student
	fields = ['firstname', 'lastname', 'adm_no', 'passport']

	def get_success_url(self):
		return reverse('crudapp:index')

	def form_valid(self, form):
		return super().form_valid(form)




