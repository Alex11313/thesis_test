from django.db import models
from django.apps import apps
import uuid


class Department(models.Model):
    """
    Модель департамента
    """

    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=100, blank=True, null=True)
    director = models.ForeignKey('employees.Employee', related_name='director',
                                 on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Модель сотрудников
    """

    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    patronymic = models.CharField('Patronymic', max_length=50, blank=True, null=True)
    position = models.CharField('Position', max_length=100, blank=True, null=True)
    salary = models.FloatField('Salary', default=0.0)
    age = models.IntegerField('Age', blank=True, null=True)
    department = models.ForeignKey('employees.Department', on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.FileField('Photo', upload_to='Employee/photo', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
