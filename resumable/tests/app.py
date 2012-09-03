# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic.edit import FormView
from django.forms import Form
from django.core.urlresolvers import reverse

from resumable.views import ResumableUploadView
from resumable.fields import ResumableFileField


class ResumableForm(Form):
    file = ResumableFileField(
        allowed_mimes=("audio/ogg",),
        upload_url=lambda: reverse('upload'),
        chunks_dir=getattr(settings, 'FILE_UPLOAD_TEMP_DIR')
    )


class TestFormView(FormView):
    form_class = ResumableForm
    template_name = 'form.html'

    @property
    def success_url(self):
        return reverse('form')


urlpatterns = patterns('',
    url('^$', TestFormView.as_view(), name='form'),
    url('^upload/$', ResumableUploadView.as_view(), name='upload')
)
