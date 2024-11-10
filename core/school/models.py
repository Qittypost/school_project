from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=63)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

class Grade(models.Model):
    numbers = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField()
