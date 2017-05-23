from django.conf.urls import url
from event_section import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^active-events/$', views.ActiveEventList.as_view()),
    # url(r'^task-interventions/$', views.TaskInterventionList.as_view()),
    # url(r'^media-interventions/$', views.MediaInterventionList.as_view()),
    # url(r'^question-interventions/$', views.QuestionInterventionList.as_view()),

    url(r'^active-events/(?P<pk>[0-9]+)/$', views.ActiveEventDetail.as_view()),
    # url(r'^task-interventions/(?P<pk>[0-9]+)/$', views.TaskInterventionDetail.as_view()),
    # url(r'^media-interventions/(?P<pk>[0-9]+)/$', views.MediaInterventionDetail.as_view()),
    # url(r'^question-interventions/(?P<pk>[0-9]+)/$', views.QuestionInterventionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)