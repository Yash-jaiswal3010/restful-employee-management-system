from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet
from django.urls import path, include
from .views import AdminDashboardView, AdminAttendanceViewSet

router = DefaultRouter()
router.register("attendence", AttendanceViewSet)

urlpatterns = [
    path('admin/dashboard/', AdminDashboardView.as_view()),
    path('', include(router.urls)),
]

