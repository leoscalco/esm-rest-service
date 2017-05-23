from django.conf.urls import url
from program_section import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^program/$', views.ProgramList.as_view()),
    url(r'^program/(?P<pk>[0-9]+)/$', views.ProgramDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)