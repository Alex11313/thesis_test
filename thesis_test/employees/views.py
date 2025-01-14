from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

from employees.models import Employee, Department
from employees.pagination import EmployeePagination
from employees.serializers import EmployeeSerializer, DepartmentSerializer

from drf_yasg import openapi


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


number_response = openapi.Response(description="custom 200 description",
        examples={
            "application/json": {
                'number': 123,
            }
        })


class NumberViewSet(APIView):
    permission_classes = [permissions.AllowAny, ]

    @swagger_auto_schema(operation_description="get number", responses={200: number_response})
    def get(self, request, format=None):
        """GET запрос через class """
        response = {
           'number': 123
        }
        return Response(response)
