from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import io

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# model object - single student data


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

    # alternative to above two lines
    # return JsonResponse(serializer.data)


# queryset - all student data


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")

    # alternative to above two lines
    return JsonResponse(serializer.data, safe=False)


# deserilize
@csrf_exempt  #bypass
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print("json data: ", json_data)
        stream = io.BytesIO(json_data)
        print("stream: ", stream)
        python_data = JSONParser().parse(stream)
        print("python data: ", python_data)
        serializer = StudentSerializer(data=python_data)
        print("serializer: ", serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")