from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView

from .models import Student, Course
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


class SignUp(SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_message = 'SIGN UP SUCCESSFULL'
    success_url = reverse_lazy('login')



class Admno(FormView):
    template_name = 'registration/admno.html'
    success_url = reverse_lazy('ncas:signup')
    form_class = AdmnoVerification


def admnoverification(request):
    if request.method == "POST":
        admno = AdmnoVerification(request.POST)
        adlist = Student.objects.all().values_list('adm_no', flat=True)
        if admno.is_valid():
            a = admno.cleaned_data['adm_no']
            if a in adlist:
                form = UserCreationForm()
                return render(request, 'registration/signup.html', {'form': form})
            else:
                return render(request, 'registration/admno.html', {'form': admno, 'valid': True})
        else:
            return render(request, 'registration/admno.html', {'form': admno})
    else:
        f=AdmnoVerification()
        # return HttpResponse('NOT A POST METHOD')
        return render(request, 'registration/admno.html', {'form': f})
