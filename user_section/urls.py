from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from user_section import views

urlpatterns = [
    url(r'^observers/$', views.ObserverList.as_view()),
    url(r'^observers/(?P<pk>[0-9]+)/$', views.ObserverDetail.as_view()),
    url(r'^observers/search/findByEmail/$', views.ObserverByEmail.as_view()),
    url(r'^participants/search/findByEmail/$', views.ParticipantByEmail.as_view()),
    url(r'^participants/$', views.ParticipantList.as_view()),
    url(r'^participants/(?P<pk>[0-9]+)/$', views.ParticipantDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
