from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass
    def retrieve(self, request):
        pass
    def update(self, request):
        pass
    def destroy(self, request):
        pass
