from rest_framework import serializers
from test_web_app.models.topic import Topic
from test_web_app.models.district import District


class TopicSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            'id',
            'date',
            'tags',
            'state',
            'location'
        )
        read_only_fields = (
            'id',
        )

    @staticmethod
    def get_location(obj):
        municipality_name = obj.municipality.name
        district = District.objects.get(pk=obj.municipality.district.pk)
        location_dict = {
            'municipality_name': municipality_name,
            'district_name': district.name
        }

        return location_dict
