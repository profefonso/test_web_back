from django.contrib import admin
from test_web_app.models.tag import Tag
from test_web_app.models.topic import Topic
from test_web_app.models.district import District
from test_web_app.models.municipality import Municipality


admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(District)
admin.site.register(Municipality)
