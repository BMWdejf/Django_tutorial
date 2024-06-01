from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Project

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    def list(self, request):
        pass
    def create(self, request):
        pass
    def retrieve(self, request):
        pass
    def update(self, request):
        pass
    def destroy(self, request):
        pass
