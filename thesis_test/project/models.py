import uuid

from django.db import models


class Project(models.Model):
    """
    Модель проекта
    """
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=100, blank=True, null=True)
    department = models.ForeignKey('employees.Department', related_name='projects',
                                   on_delete=models.SET_NULL, blank=True, null=True)
    employees = models.ManyToManyField('employees.Employee')
    boss = models.ForeignKey('employees.Employee', related_name='project_host',
                             on_delete=models.SET_NULL, blank=True, null=True)
