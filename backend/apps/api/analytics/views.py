from django.db.models import Prefetch, Count
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins

from api.base.views import BaseApiViewSet
from db.articles.models import Post
from db.users.models import User
from .serializers import PostAnalyticsSerializer, PostFilterSerializer


class AnalyticsView(
    mixins.ListModelMixin,
    BaseApiViewSet
):
    serializer_class = PostAnalyticsSerializer
    queryset = Post.objects.prefetch_related(
        Prefetch('users_liked', queryset=User.objects.only('id')),
        Prefetch('users_unliked', queryset=User.objects.only('id'))
    )
    filter_serializer_class = PostFilterSerializer

    def get_queryset(self):
        qs = self.filter_queryset(super().get_queryset())
        qs = qs.annotate(
            likes_count=Count('users_liked'),
            unlikes_count=Count('users_unliked'),
        )
        return qs

    @extend_schema(
        parameters=[
            OpenApiParameter('date_from', type=OpenApiTypes.DATE),
            OpenApiParameter('date_to', type=OpenApiTypes.DATE)
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
