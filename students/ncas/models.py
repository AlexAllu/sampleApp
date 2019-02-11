from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator


class Course(models.Model):
    c_name = models.CharField('COURSE', max_length=4)
    c_id = models.CharField('COURSE ID', primary_key=True, max_length=3)

    def __str__(self):
        return self.c_name


ch = (('Not selected', 0),
      ('Sem 1', 1),
      ('Sem 2', 2),
      ('Sem 3', 3),
      ('Sem 4', 4),
      ('Sem 5', 5),
      ('Sem 6', 6)
      )


class Student(models.Model):
    name = models.CharField('NAME', max_length=30)
    reg_no = models.IntegerField('REGISTER NO', validators=[MinValueValidator(1), MaxValueValidator(1000)], unique=True)
    adm_no = models.IntegerField('ADMISSION NO', primary_key=True)
    adrs = models.CharField('ADDRESS', max_length=200)
    sem = models.CharField('Current Sem', choices=ch, default=0, max_length=10)
    course = models.ForeignKey(Course, verbose_name='COURSE', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    s_id = models.IntegerField('SUBJECT CODE', primary_key=True)
    s_name = models.CharField('SUBJECT NAME', max_length=30)
    sem = models.CharField('SEM', choices=ch, default=0, max_length=10)
    s_mark1 = models.IntegerField('FIRST INTERNAL', default=0, validators=[MaxValueValidator(50),MinValueValidator(0)])
    s_mark2 = models.IntegerField('SECOND INTERNAL', default=0, validators=[MaxValueValidator(50),MinValueValidator(0)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Branch', null=True)

    def __str__(self):
        return self.s_name
