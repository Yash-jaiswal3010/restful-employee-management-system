from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceSerializer
from datetime import time
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from employees.models import Employee
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        employee = self.request.user.employee_profile
        current_time = timezone.now().time()

        if current_time > time(9, 30):
            status = 'Late'
        else:
            status = 'Present'

        serializer.save(
            employee=employee,
            check_in=current_time,
            status=status
        )

    # checkout time detection
    @action(detail=True, methods=['patch'])
    def checkout(self, request, pk=None):
        attendance = self.get_object()

        attendance.check_out = timezone.now().time()
        attendance.save()

        return Response({"message": "Checked out successfully"})
    
    # ui making

class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request):
        today = timezone.now().date()

        total_employees = Employee.objects.count()
        present = Attendance.objects.filter(date=today, status='Present').count()
        late = Attendance.objects.filter(date=today, status='Late').count()

        checked_in_ids = Attendance.objects.filter(date=today).values_list('employee_id', flat=True)
        absent = Employee.objects.exclude(id__in=checked_in_ids).count()

        return Response({
            "total_employees": total_employees,
            "present": present,
            "late": late,
            "absent": absent
        })
# Attendance List API (Admin view)

class AdminAttendanceViewSet(ReadOnlyModelViewSet):
    queryset = Attendance.objects.all().select_related('employee')
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'employee']

# Filters addition
