from django.contrib import admin
from .models import Student, Course,Subject,Semester

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Semester)