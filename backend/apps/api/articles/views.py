from django.db import transaction
from django.db.models import Prefetch
from rest_framework import response, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from api.articles.serializers import PostSerializer
from api.base.views import BaseApiViewSet
from db.articles.models import Post
from db.users.models import User


class PostView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseApiViewSet
):
    serializer_class = PostSerializer
    queryset = Post.objects.prefetch_related(
        Prefetch('users_liked', queryset=User.objects.only('id')),
        Prefetch('users_unliked', queryset=User.objects.only('id'))
    )
    permission_classes = (IsAuthenticated,)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.users_unliked.remove(self.request.user)
        post.users_liked.add(self.request.user)
        return response.Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.users_liked.remove(self.request.user)
        post.users_unliked.add(self.request.user)
        return response.Response(status=status.HTTP_200_OK)
