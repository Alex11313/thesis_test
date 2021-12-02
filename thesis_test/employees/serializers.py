"""
Account API serializers
"""
from django.db.models import Sum
from rest_framework import serializers

from employees.models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('uid', 'name', 'surname', 'patronymic', 'position', 'salary', 'age', 'department', 'photo', )
        read_only_fields = ('uid', )
        lookup_field = 'uid'


class DepartmentSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    salary_sum = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('uid', 'name', 'count', 'salary_sum', 'director')
        read_only_fields = ('uid', )
        lookup_field = 'uid'

    @staticmethod
    def get_salary_sum(obj):
        department_employees = obj.employee_set.all()
        salary_sum = department_employees.aggregate(Sum('salary')).get('salary__sum')
        if salary_sum is None:
            salary_sum = 0
        return salary_sum

    @staticmethod
    def get_count(obj):
        return obj.employee_set.all().count()
