# -*- coding: utf-8 -*-
from django.forms.fields import FileField

from widgets import ResumableFileInput


class ResumableFileField(FileField):
    widget = ResumableFileInput

    @property
    def upload_url(self):
        if not 'upload_url' in self.widget.attrs:
            raise Exception("You must set the upload url.")
        return self.widget.attrs['upload_url']

    @upload_url.setter
    def upload_url(self, url):
        self.widget.attrs['upload-url'] = url

    @property
    def chunks_dir(self):
        if not hasattr(self.widget, 'chunks_dir'):
            raise Exception("You must set a `chunk_dir`.")
        return self.widget.storage

    @chunks_dir.setter
    def chunks_dir(self, chunks_dir):
        self.widget.chunks_dir = chunks_dir
