from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mentor = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    subcode = models.CharField(max_length=10)
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)