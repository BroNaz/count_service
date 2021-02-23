
from django.urls import path, include
from .views import StatisticSaveView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('statistics', StatisticSaveView)




urlpatterns = router.urls
