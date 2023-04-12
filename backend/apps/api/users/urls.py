# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserSignUpView, UserLastLoginView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

router = SimpleRouter()
router.register(r"sign-up", UserSignUpView, basename="users")
router.register(r"last-login", UserLastLoginView, basename="last_login")
urlpatterns += router.urls
