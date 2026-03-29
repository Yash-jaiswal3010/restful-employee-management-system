from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
