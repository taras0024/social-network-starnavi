from rest_framework import serializers

from db.articles.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title',)

    def create(self, validated_data):
        validated_data['creator'] = self.context['user']
        return super().create(validated_data)
