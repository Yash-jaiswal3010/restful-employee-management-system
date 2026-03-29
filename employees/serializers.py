from rest_framework import serializers
from .models import Employee
from departments.serializers import DepartmentSerializer
from departments.models import Department
# i need the id,username,email and i have one to one relation  so 
#i will use nested serializer to get those detail and converting in api
# hamne ek serializer ki madad se dusra serializer banya haii isliye ye nested serializer hai
# from accounts.serializers import UserSerializer---- baad me handel karenge


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset = Department.objects.all(),
        source='department',
        write_only = True
    )
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ["user"]