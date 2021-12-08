"""Джанго Админка"""
from django.contrib import admin

from .models import Employee, Department
from project.models import Project


class ProjectInline(admin.TabularInline):
    model = Project


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Доступ к модели Department через административную панель"""
    list_display = ('uid', 'name', )
    fields = ('uid', 'name', 'director', )
    search_fields = ('name', )
    readonly_fields = ('uid', )
    inlines = [ProjectInline]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Доступ к модели Employee через административную панель"""
    list_display = ('uid', 'name', )
    fields = ('uid', 'name', 'surname', 'patronymic', 'position',
              'salary', 'age', 'department', 'photo', )
    search_fields = ('uid', 'name', 'surname', 'patronymic', 'position', 'department', )
    readonly_fields = ('uid', )
