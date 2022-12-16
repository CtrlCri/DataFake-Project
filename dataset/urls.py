from rest_framework import routers
from .api import DatasetViewSet

router = routers.DefaultRouter()

router.register('api/dataset', DatasetViewSet, 'dataset')

urlpatterns = router.urls
