from django.shortcuts import render

from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

from .models import Student
from django_filters.rest_framework import DjangoFilterBackend


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)

    # using django filter
    filter_backends = [DjangoFilterBackend]  #locally (per view)
    filterset_fields = ['city', 'name']
