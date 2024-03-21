from django.shortcuts import render
from django.http import HttpResponse
from pets_for_students.models import Cats, Student

def index(request):
    students = Student.objects.order_by('last_name')
    cats = Cats.objects.order_by('name')
    context_dict = {
        'students' : students,
        'cats' : cats,
    }
    return render(request, 'pets_for_students/index.html', context=context_dict)


def pets(request):
    cats = Cats.objects.order_by('name')
    context_dict = {
        'cats' : cats,
    }
    return render(request, 'pets_for_students/pets.html', context=context_dict)