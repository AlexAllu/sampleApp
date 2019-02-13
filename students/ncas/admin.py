from django.contrib import admin
from .models import Student, Course, Subject, Mark

# Register your models here.
#admin.site.register(StudentR)
admin.site.register(Course)
admin.site.register(Subject)


# admin.site.register(Mark)

class MarkInline(admin.TabularInline):
    model = Mark
    fields = ['sem', 'sub', 's_mark1', 's_mark2']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [MarkInline]
