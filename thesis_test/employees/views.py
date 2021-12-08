from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from employees.models import Employee, Department
from employees.pagination import EmployeePagination
from employees.serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Employee CRUD methods.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['surname', 'department__uid', 'department__name', ]

    permission_classes = [IsAuthenticated]

    pagination_class = EmployeePagination

    lookup_field = 'uid'


class DepartmentViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    """
    Department GET, LIST methods.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    permission_classes = [AllowAny]

    lookup_field = 'uid'
