from django.conf.urls import url
from intervention_section import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^interventions/$', views.InterventionList.as_view()),

    url(r'^empty-interventions/$', views.EmptyInterventionList.as_view()),
    url(r'^task-interventions/$', views.TaskInterventionList.as_view()),
    url(r'^media-interventions/$', views.MediaInterventionList.as_view()),
    url(r'^question-interventions/$', views.QuestionInterventionList.as_view()),

    url(r'^empty-interventions/(?P<pk>[0-9]+)/$', views.EmptyInterventionDetail.as_view()),
    url(r'^task-interventions/(?P<pk>[0-9]+)/$', views.TaskInterventionDetail.as_view()),
    url(r'^media-interventions/(?P<pk>[0-9]+)/$', views.MediaInterventionDetail.as_view()),
    url(r'^question-interventions/(?P<pk>[0-9]+)/$', views.QuestionInterventionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)