from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView

from .models import Student, Course, Subject, Mark
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StudentCreation, UserCreationForm, MarkCreation


class StudentDetail(generic.DetailView):
    model = Student
    template_name = 'ncas/studentdetails.html'
    context_object_name = 'student'


def user_create(request):
    if request.method == "POST":
        sign = UserCreationForm(request.POST)
        if sign.is_valid():
            sign.save()
            u = sign.cleaned_data.get('username')
            p = sign.cleaned_data.get('password1')
            user = authenticate(username=u, password=p)
            return redirect('ncas:studentcreate', pk=user.id)
        else:
            return render(request, 'ncas/signup.html', {'form': sign})
    else:
        sign = UserCreationForm()
        return render(request, 'ncas/signup.html', {'form': sign})


def student_create(request, pk):
    if request.method == "POST":
        form = StudentCreation(request.POST)
        student = Student()
        student.details = User.objects.get(id=pk)
        student.tutor = request.user.tutor       # User.objects.get(id=request.user.id)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.reg_no = form.cleaned_data['reg_no']
            student.adm_no = form.cleaned_data['adm_no']
            student.course = form.cleaned_data['course']
            student.save()
            return redirect('ncas:studentdetail', pk=student.pk)
        else:
            return render(request, 'ncas/studen_create.html', {'form': form})
    else:
        form = StudentCreation()
        return render(request, 'ncas/studen_create.html', {'form': form})


def studentlist(request):
    li = request.user.tutor.student_set.all()
    return render(request, 'ncas/studentlist.html', {'list': li})


def mark_create(request, pk):
    mark = Mark()
    ob = Student.objects.get(pk=pk)

    mark.student = ob
    sub_list = ob.course.subject_set.all()
    if request.method == "POST":
        form = MarkCreation(request.POST, list1=sub_list)
        mark.details = ob
        if form.is_valid():
            mark.sub = form.cleaned_data['sub']
            mark.sem = (form.cleaned_data['sub']).sem
            mark.s_mark1 = form.cleaned_data['s_mark1']
            mark.s_mark2 = form.cleaned_data['s_mark2']
            mark.save()
            return redirect('ncas:studentdetail', pk=pk)
        else:
            return render(request, 'ncas/mark_create.html', {'form': form})
    else:
        form = MarkCreation(list1=sub_list)
        return render(request, 'ncas/mark_create.html', {'form': form})

