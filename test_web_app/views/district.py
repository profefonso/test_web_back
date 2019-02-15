from rest_framework import generics
from test_web_app.models.district import District
from test_web_app.serializers.district import DistrictSerializer


class DistrictList(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    name = 'district-list'


class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    name = 'district-detail'
