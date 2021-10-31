from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'project-employee-configuration', views.ProjectEmployeeViewSet)
router.register(r'timesheet-set', views.TimeSheetSetViewSet)

urlpatterns = [
    # path('otp/<str:uid>/', views.otp, name='doctor_otp'),
    path('', include(router.urls)),
]