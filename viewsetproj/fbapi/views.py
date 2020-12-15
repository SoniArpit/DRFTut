# ViewSet in Django REST Framework

from .models import Student
from .serializers import StudentSerializer

from rest_framework.response import Response

from rest_framework import status, viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("---------List---------")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("---------retrieve---------")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            # print(serializer.data)
            return Response(serializer.data)

    def create(self, request):
        print("---------create---------")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print("---------update---------")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, format=None):
        print("---------partial update---------")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, format=None):
        print("---------destroy---------")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
