from django.db import models
from django.conf import settings
from departments.models import Department

class Employee(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee_profile'
    )

    # establishing relationship with department
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    date_joined = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
