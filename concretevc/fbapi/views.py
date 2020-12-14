# Concrete View Class

from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# all together - short (combine class)


class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRU(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# retrieve update and delete together instead of above two class
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'pk'
    serializer_class = StudentSerializer