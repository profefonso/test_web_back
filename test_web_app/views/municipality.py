from rest_framework import generics
from test_web_app.models.district import District
from test_web_app.models.municipality import Municipality
from test_web_app.serializers.municipality import MunicipalitySerializer


class MunicipalityList(generics.ListCreateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    name = 'municipality-list'

    def get_queryset(self):
        queryset = Municipality.objects.all()
        id_district = self.request.query_params.get('id_district', None)
        if id_district is not None:
            district = District.objects.get(pk=id_district)
            queryset = queryset.filter(district=district)
        return queryset


class MunicipalityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    name = 'municipality-detail'
