from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from program_section import views

urlpatterns = [
    url(r'^programs/$', views.ProgramList.as_view()),
    url(r'^programs/(?P<pk>[0-9]+)/$', views.ProgramDetail.as_view()),
    url(r'^programs/search/findByObserversEmail/$', views.ProgramsByEmail.as_view()),
    url(r'^programs/search/findByParticipantsEmail/$', views.ProgramsByParticipantEmail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
