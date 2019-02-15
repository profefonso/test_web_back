from django.urls import path
from django.contrib import admin
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

from test_web_app.views import district
from test_web_app.views import municipality
from test_web_app.views import tag
from test_web_app.views import topic

schema_view = get_swagger_view(title='TEST WEB API')


urlpatterns = [
    path('front/betsy/irish/embargo/admin/', admin.site.urls),

    # Swagger API
    path(
        'api/',
        schema_view,
        name='api'
    ),

    # district
    path(
        'district/',
        district.DistrictList.as_view(),
        name=district.DistrictList.name
    ),
    re_path(
        '^district/(?P<pk>[0-9]+)/$',
        district.DistrictDetail.as_view(),
        name=district.DistrictDetail.name
    ),
    # district
    path(
        'municipality/',
        municipality.MunicipalityList.as_view(),
        name=municipality.MunicipalityList.name
    ),
    re_path(
        '^municipality/(?P<id_district>.+)/$',
        municipality.MunicipalityDetail.as_view(),
        name=municipality.MunicipalityDetail.name
    ),
    re_path(
        '^municipality/(?P<pk>[0-9]+)/$',
        municipality.MunicipalityDetail.as_view(),
        name=municipality.MunicipalityDetail.name
    ),
    # tag
    path(
        'tag/',
        tag.TagList.as_view(),
        name=tag.TagList.name
    ),
    re_path(
        '^tag/(?P<pk>[0-9]+)/$',
        tag.TagDetail.as_view(),
        name=tag.TagDetail.name
    ),
    # topic
    path(
        'topic/',
        topic.TopicList.as_view(),
        name=topic.TopicList.name
    ),
    re_path(
        '^topic/(?P<pk>[0-9]+)/$',
        topic.TopicDetail.as_view(),
        name=topic.TopicDetail.name
    ),
]
