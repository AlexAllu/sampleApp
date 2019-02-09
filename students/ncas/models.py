from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator


class Course(models.Model):
    c_name = models.CharField('COURSE', max_length=4)
    c_id = models.CharField('COURSE ID', primary_key=True, max_length=3)

    def __str__(self):
        return self.c_name


class Student(models.Model):
    name = models.CharField('NAME', max_length=30)
    reg_no = models.CharField('REGISTER NO', max_length=30, unique=True)
    adm_no = models.IntegerField('ADMISSION NO', primary_key=True)
    adrs = models.CharField('ADDRESS', max_length=200)
    course = models.ForeignKey(Course, verbose_name='COURSE', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    s_id = models.IntegerField('SUBJECT CODE', primary_key=True)
    s_name = models.CharField('SUBJECT NAME', max_length=30)
    s_mark1 = models.IntegerField('FIRST INTERNAL', default=0)
    s_mark2 = models.IntegerField('SECOND INTERNAL', default=0)

    def __int__(self):
        return self.s_id


class Semester(models.Model):
    course = models.ForeignKey(Course, verbose_name='COURSE', on_delete=models.CASCADE)
    semno = models.IntegerField('SEMNO', primary_key=True)
    s_id = models.ManyToManyField(Subject)

    def __int__(self):
        return self.semno
