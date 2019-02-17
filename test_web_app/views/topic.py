from rest_framework import status
from rest_framework import generics
from test_web_app.models.topic import Topic
from rest_framework.response import Response
from test_web_app.models.municipality import Municipality
from test_web_app.serializers.topic import TopicSerializer
from rest_framework.pagination import PageNumberPagination


class TopicPagination(PageNumberPagination):
    page_size = 5


class TopicList(generics.ListCreateAPIView):
    pagination_class = TopicPagination
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    name = 'topic-list'

    def get_queryset(self):
        queryset = Topic.objects.filter(state='active').order_by('-id')
        return queryset

    def create(self, request):
        print(request.data)
        try:
            data = request.data
            id_municipality = int(data['municipality'])
            municipality = Municipality.objects.get(pk=id_municipality)
            topic = Topic()
            topic.date = str(data['date'])[:10]
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
