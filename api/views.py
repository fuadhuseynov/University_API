from django.shortcuts import render
from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope, permissions


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer