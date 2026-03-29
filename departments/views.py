from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.exceptions import PermissionDenied
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            if not self.request.user.is_staff:
                raise PermissionDenied("Only admin can modify departments")
        return [IsAuthenticated()]
    


# Create your views here.
