from rest_framework import status
from rest_framework import generics
from test_web_app.models.topic import Topic
from rest_framework.response import Response
from test_web_app.models.municipality import Municipality
from test_web_app.serializers.topic import TopicSerializer
from rest_framework.pagination import PageNumberPagination


class TopicPagination(PageNumberPagination):
    page_size = 3


class TopicList(generics.ListCreateAPIView):
    pagination_class = TopicPagination
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    name = 'topic-list'

    def create(self, request):
        try:
            data = request.data
            municipality = Municipality.objects.get(pk=data['municipality'])
            topic = Topic()
            topic.date = data['date']
            topic.tags = data['tags']
            topic.state = data['state']
            topic.municipality = municipality
            topic.save()
            return Response({'successful'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    name = 'topic-detail'

    def update(self, request,  *args, **kwargs):
        try:
            data = request.data
            topic = Topic.objects.get(pk=data['id'])
            topic.state = data['state']
            topic.save()
            return Response({'successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
