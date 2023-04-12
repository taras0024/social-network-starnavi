from django.db import transaction
from rest_framework import response, mixins, status

from api.base.views import BaseApiViewSet
from db.users.models import User
from .serializers import UserSignUpSerializer, UserSerializer


class UserSignUpView(mixins.CreateModelMixin, BaseApiViewSet):
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class UserLastLoginView(mixins.ListModelMixin, BaseApiViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
