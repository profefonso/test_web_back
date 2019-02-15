from rest_framework import serializers
from test_web_app.models.tag import Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )
