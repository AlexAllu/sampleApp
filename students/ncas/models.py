import uuid as uuid

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator


class Course(models.Model):
    name = models.CharField('Name', max_length=10)
    hod = models.CharField('HOD', max_length=20)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    detail = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    details = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100)
    adm_no = models.IntegerField('Admission No', validators=[MinValueValidator(1), MaxValueValidator(1000)])
    reg_no = models.IntegerField('Reg No', primary_key=True)
    course = models.ForeignKey(Course, verbose_name='Course', on_delete=models.PROTECT)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name='Tutor')

    def __str__(self):
        return self.name


class Subject(models.Model):
    ch = ((1, 'Semester 1'),
          (2, 'Semester 2'),
          (3, 'Semester 3'),
          (4, 'Semester 4'),
          (5, 'Semester 5'),
          (6, 'Semester 6'))
    name = models.CharField('Name', max_length=20)
    course = models.ForeignKey(Course, verbose_name='Course', on_delete=models.CASCADE, blank=False)
    sem = models.IntegerField('Sem', choices=ch, default=0)

    def __str__(self):
        return self.name


class Mark(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    student = models.ForeignKey(Student, verbose_name='Student', on_delete=models.CASCADE)
    sub = models.ForeignKey(Subject, verbose_name='Subject', on_delete=models.CASCADE)
    s_mark1 = models.IntegerField('First Internal mark', validators=[MaxValueValidator(50), MinValueValidator(0)], null=True)
    s_mark2 = models.IntegerField('Second Internal mark', validators=[MaxValueValidator(50), MinValueValidator(0)], null=True)

    def __str__(self):
        return self.sub.name
