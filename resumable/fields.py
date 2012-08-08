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
    def storage(self):
        if not hasattr(self.widget, 'storage'):
            raise Exception("You must set the storage.")
        return self.widget.storage

    @storage.setter
    def storage(self, storage):
        self.widget.storage = storage
