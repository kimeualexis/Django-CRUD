from django.shortcuts import render
from . models import Student
from . forms import StudentForm


# Create your views here.
def index(request):
	students = Student.objects.all()
	return render(request, 'crudapp/index.html',
				  {'students': students})


def add_student(request):
	form = StudentForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		student = form.save(commit=False)
		student.passport = request.FILES['passport']
		student.save()
		students = Student.objects.all()
		return render(request, 'crudapp/index.html', {'students': students})
	return render(request, 'crudapp/add_student.html', {'form':
														form})




