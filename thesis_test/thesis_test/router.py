from rest_framework import routers

from employees.router import register as employee_register

router = routers.DefaultRouter()

employee_register(router)
