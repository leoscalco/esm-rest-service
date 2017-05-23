from django.conf.urls import url
from trigger_section import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^triggers/$', views.EventTriggerList.as_view()),
    url(r'^triggers/(?P<pk>[0-9]+)/$', views.EventTrigerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)