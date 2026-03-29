from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)

    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'),  ('Late', 'Late'),('Absent', 'Absent')],
        default='Present'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['employee', 'date']