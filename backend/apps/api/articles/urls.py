# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from .views import PostView

router = SimpleRouter()
router.register(r"", PostView, basename="posts")
urlpatterns = router.urls
