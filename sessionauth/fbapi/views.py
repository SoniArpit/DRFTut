# Session Authentication and Permission

from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]  # access for all registered user
    # permission_classes = [IsAdminUser]  # if is_staff is true
    # permission_classes = [IsAuthenticatedOrReadOnly]  # if auth then all permission otherwise only read
    # permission_classes = [DjangoModelPermissions]  # permission according to model edit to particular user from django admin

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly
                          ]  # same as above but unauth can read only
