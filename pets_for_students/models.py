from django.db import models

class Student(models.Model):
    NAME_MAX_LENGTH = 128
    first_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    last_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    number_of_cats = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cats(models.Model):
    NAME_MAX_LENGTH=128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cats'

    def __str__(self):
        return self.name