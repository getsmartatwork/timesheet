from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'vendor', views.VendorViewSet)

urlpatterns = [
    # path('otp/<str:uid>/', views.otp, name='doctor_otp'),
    path('', include(router.urls)),
]