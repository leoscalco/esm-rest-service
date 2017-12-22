from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from result_section import views

urlpatterns = [
    url(r'^results-session/$', views.ResultSessionList.as_view()),
    url(r'^results/$', views.ResultsList.as_view()),

    url(r'^media-results/$', views.MediaResultList.as_view()),
    url(r'^task-results/$', views.TaskResultList.as_view()),
    url(r'^empty-results/$', views.EmptyResultList.as_view()),
    url(r'^sensor-results/$', views.SensorResultList.as_view()),
    url(r'^question-results/$', views.QuestionResultList.as_view()),

    url(r'^media-results/(?P<pk>[0-9]+)/$', views.MediaResultDetail.as_view()),
    url(r'^task-results/(?P<pk>[0-9]+)/$', views.TaskResultDetail.as_view()),
    url(r'^empty-results/(?P<pk>[0-9]+)/$', views.EmptyResultDetail.as_view()),
    url(r'^sensor-results/(?P<pk>[0-9]+)/$', views.SensorResultDetail.as_view()),
    url(r'^question-results/(?P<pk>[0-9]+)/$', views.QuestionResultDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
