from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import TodoSerializers
from .models import todo

class TodoView(ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializers
    