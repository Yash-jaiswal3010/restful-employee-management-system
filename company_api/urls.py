from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import RegisterView,LoginView,DashboardView
from .views import dashboard_page,login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/',LoginView.as_view(),name="auth_login"),
    path('api/auth/register/',RegisterView.as_view(),name="auth_register"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/dashboard/', DashboardView.as_view(),name="dashboard"),
    path("api/",include("employees.urls")),
    path("api/",include("departments.urls")),
    path('api/', include('attendence.urls')),
    path('dashboard-page/', dashboard_page),
    path('login-page/', login_page),
]
