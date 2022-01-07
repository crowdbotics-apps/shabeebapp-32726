from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ServicesViewSet

router = DefaultRouter()
router.register("services", ServicesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
