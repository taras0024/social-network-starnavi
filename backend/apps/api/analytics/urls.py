# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from .views import AnalyticsView

router = SimpleRouter()
router.register(r"", AnalyticsView, basename="analytics")
urlpatterns = router.urls
