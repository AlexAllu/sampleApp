from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView

from .models import Student, Course, Subject
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin



class StudentDetail(generic.DetailView):
    model = Student
    template_name = 'ncas/studentdetails.html'
    context_object_name = 'studentd'


class CourseList(generic.ListView):
    model = Course
    template_name = 'ncas/courselist.html'
    context_object_name = 'clist'

    def get_queryset(self):
        return Course.objects.all()


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'ncas/coursedetails.html'
    context_object_name = 'coursedetail'


def signUp(request):
    if request.method == "POST":
        sign = UserCreationForm(request.POST)
        if sign.is_valid():
            sign.save()
            u = sign.cleaned_data.get('username')
            p = sign.cleaned_data.get('password1')
            user = authenticate(username=u, password=p)
            login(request, user)
            return redirect('ncas:home')
        else:
            return render(request, 'registration/signup.html', {'form': sign})
    else:
        sign = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': sign})





'''def admnoverification(request):
    if request.method == "POST":
        admno = AdmnoVerification(request.POST)

        if admno.is_valid():

            if a in adlist:
                form = UserCreationForm()
                return render(request, 'registration/signup.html', {'form': form})
            else:
                return render(request, 'registration/admno.html', {'form': admno})
        else:
            return render(request, 'registration/admno.html', {'form': admno})
    else:
        f = AdmnoVerification()
        return render(request, 'registration/admno.html', {'form': f})'''

def home(request):
    return render(request, 'ncas/index.html')
