from django.db import models

def auto_str(*field_names):
    """
    Декоратор для автоматичного створення методу __str__ на основі вказаних полів.
    """
    def decorator(cls):
        # Створення методу __str__
        def __str__(self):
            field_values = ", ".join(f"{name}={getattr(self, name)}" for name in field_names)
            return f"{self.__class__.__name__}({field_values})"
        cls.__str__ = __str__
        return cls
    return decorator


@auto_str('name')
class Subject(models.Model):
    name = models.CharField(max_length=63)


@auto_str('name', 'subject')
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)


@auto_str('name', 'grade')
class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)


@auto_str('numbers', 'teacher')
class Grade(models.Model):
    numbers = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)


@auto_str('subject', 'teacher', 'date')
class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField()
