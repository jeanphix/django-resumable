# -*- coding: utf-8 -*-
from mimetypes import guess_type

from django.forms.widgets import FileInput, HiddenInput
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.utils.safestring import mark_safe


class ResumableFileInput(FileInput):
    def __init__(self, *args, **kwargs):
        super(ResumableFileInput, self).__init__(*args, **kwargs)
        self.filename = None

    def filename_input_name(self, name):
        """Returns the name of the input[type=hidden] that contains the
        uploaded file path.
        """
        return "%s-path" % name

    def value_from_datadict(self, data, files, name):
        filename = data.get(self.filename_input_name(name))
        storage = self.storage
        if filename is not None and len(filename) > 0 \
                and storage.exists(filename):
            self.filename = filename
            file = storage.open(filename)
            return UploadedFile(
                file=file,
                name = filename,
                content_type=guess_type(file.name)[0],
                size = storage.size(filename)
            )
        return files.get(name, None)

    def render(self, name, *args, **kwargs):
        return mark_safe("%s%s" % (
            HiddenInput().render(self.filename_input_name(name),
                self.filename, {}),
            super(ResumableFileInput, self).render(name, *args, **kwargs)
        ))

    @property
    def storage(self):
        return FileSystemStorage(location=self.chunks_dir)
