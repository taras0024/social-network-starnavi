from django.db import models
from rest_framework import serializers

from db.articles.models import Post


class PostFilterSerializer(serializers.Serializer):
    date_from = serializers.DateField(required=False, input_formats=['%Y-%m-%d'])
    date_to = serializers.DateField(required=False, input_formats=['%Y-%m-%d'])
    query = serializers.CharField(required=False, max_length=100, allow_blank=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        db_filters, extra_filters, query_filter = models.Q(), dict(), models.Q()

        date_from = attrs.get('date_from')
        date_to = attrs.get('date_to')

        if all((date_from, date_to)):
            if date_from > date_to:
                raise serializers.ValidationError({
                    {'date': 'date_from must be less than date_to'}
                })
            db_filters |= models.Q(likes__created_at__date__range=(date_from, date_to))
            db_filters |= models.Q(unlikes__created_at__date__range=(date_from, date_to))

        if date_from and not date_to:
            db_filters |= models.Q(likes__created_at__date__gte=attrs['date_from'])
            db_filters |= models.Q(unlikes__created_at__date__gte=attrs['date_from'])

        if date_to and not date_from:
            db_filters |= models.Q(likes__created_at__lte=attrs['date_to'])
            db_filters |= models.Q(unlikes__created_at__lte=attrs['date_to'])

        return {"db_filters": db_filters, "db_query": query_filter, "db_extra": extra_filters}


class PostAnalyticsSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    unlikes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'likes_count', 'unlikes_count')
