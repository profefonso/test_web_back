from rest_framework import generics
from test_web_app.models.tag import Tag
from test_web_app.serializers.tag import TagSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    name = 'tag-list'


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    name = 'tag-detail'
