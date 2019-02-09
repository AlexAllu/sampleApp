from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView

from .models import Student, Course, Subject, Semester
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AdmnoVerification


class StdView(LoginRequiredMixin, generic.ListView):
    template_name = 'ncas/detailsl.html'
    context_object_name = 'std'

    def get_queryset(self):
        return Student.objects.all()


class StdDView(generic.DetailView):
    model = Student
    template_name = 'ncas/details.html'
    context_object_name = 'detd'


class CoursView(LoginRequiredMixin, generic.ListView):
    template_name = 'ncas/coursel.html'
    context_object_name = 'courslist'

    def get_queryset(self):
        return Course.objects.all()


class CoursDView(generic.DetailView):
    model = Course
    template_name = 'ncas/course.html'


def signUp(request):
    if request.method == "POST":
        sign = UserCreationForm(request.POST)
        if sign.is_valid():
            sign.save()
            u = sign.cleaned_data.get('username')
            p = sign.cleaned_data.get('password1')
            user = authenticate(username=u, password=p)
            login(request, user)
            return redirect('ncas:std')
        else:
            return render(request, 'registration/signup.html', {'form': sign})
    else:
        sign = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': sign})


'''class Admno(FormView):
    template_name = 'registration/admno.html'
    success_url = reverse_lazy('ncas:signup')
    form_class = AdmnoVerification'''


def admnoverification(request):
    if request.method == "POST":
        admno = AdmnoVerification(request.POST)
        adlist = Student.objects.all().values_list('adm_no', flat=True)
        if admno.is_valid():
            a = admno.cleaned_data.get('adm_no')
            if a in adlist:
                form = UserCreationForm()
                return render(request, 'registration/signup.html', {'form': form})
            else:
                return render(request, 'registration/admno.html', {'form': admno})
        else:
            return render(request, 'registration/admno.html', {'form': admno})
    else:
        f = AdmnoVerification()
        return render(request, 'registration/admno.html', {'form': f})


class SemView(generic.ListView):
    template_name = 'ncas/sem.html'
    context_object_name = 'semv'

    def get_queryset(self):
        return SemView.objects.all()


class SemDLView(generic.ListView):
    template_name = 'ncas/semd.html'
    context_object_name = 'semd'

    def get_queryset(self):
        return SemDLView.objects.all()
