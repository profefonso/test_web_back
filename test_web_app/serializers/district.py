from rest_framework import serializers
from test_web_app.models.district import District


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = (
            'id',
            'name',
            'iso_district_code',
        )
        read_only_fields = (
            'id',
        )
