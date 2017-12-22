from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from sensor_section import views

urlpatterns = [
    url(r'^sensors/$', views.SensorList.as_view()),
    url(r'^sensors/(?P<pk>[0-9]+)/$', views.SensorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
