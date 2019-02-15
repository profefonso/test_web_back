from rest_framework import serializers
from test_web_app.models.municipality import Municipality


class MunicipalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipality
        fields = (
            'id',
            'district',
            'name',
            'comments'
        )
        read_only_fields = (
            'id',
        )
