
# backend/server/apps/knn/urls.py file
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.knn.views import EndpointViewSet
from apps.knn.views import MLAlgorithmViewSet
from apps.knn.views import MLAlgorithmStatusViewSet
from apps.knn.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"knn", EndpointViewSet, basename="knn")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]
