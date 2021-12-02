from employees.views import DepartmentViewSet, EmployeeViewSet


def register(router):
    router.register('department', DepartmentViewSet, basename='department')
    router.register('employee', EmployeeViewSet, basename='employee')
