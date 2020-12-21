"""viewsetproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fbapi import views

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('stuapi', views.StudentModelViewSet, basename="studentapi")

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('auth/', include("rest_framework.urls", namespace="rest_framework"))
    path('admin/', admin.site.urls),
    path('stuapi/', views.StudentList.as_view()),  # for list and create
    path('stuapi/create/', views.StudentCreate.as_view()),
    path('stuapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('stuapi/<int:pk>/',
    #      views.StudentRU.as_view()),  # for retrieve, update,
    # path('stuapi/<int:pk>/',
    #      views.StudentRD.as_view()),  # for retrieve, delete,
    # path('stuapi/<int:pk>/',
    #      views.StudentRUD.as_view()),  # for retrieve, update, destroy

    # path('stuapi/<int:pk>/', views.StudentRetrieve.as_view()),
]
