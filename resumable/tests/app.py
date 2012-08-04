# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from resumable.views import ResumableUploadView


urlpatterns = patterns('',
    url('upload/', ResumableUploadView.as_view(), name='upload')
)
