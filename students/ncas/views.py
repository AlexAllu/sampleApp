from django.shortcuts import render
from django.views import generic
from .models import Student, Course


class StdView(generic.ListView):
    template_name = 'ncas/detailsl.html'
    context_object_name = 'std'

    def get_queryset(self):
        return Student.objects.all()


class StdDView(generic.DetailView):
    model = Student
    template_name = 'ncas/details.html'


class CoursView(generic.ListView):
    template_name = 'ncas/coursel.html'
    context_object_name = 'courslist'

    def get_queryset(self):
        return Course.objects.all()


class CoursDView(generic.DetailView):
    model = Course
    template_name = 'ncas/course.html'
