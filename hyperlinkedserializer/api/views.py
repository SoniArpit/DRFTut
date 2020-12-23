from django.shortcuts import render
from .serializers import StudentSerailizer
from rest_framework import viewsets
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizer