# -*- coding: utf-8 -*-
from mimetypes import guess_type

from django.forms.widgets import FileInput, CheckboxInput
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile


class ResumableFileInput(FileInput):
    def path_input_hidden_name(self, name):
        """Returns the name of the input[type=hidden] that contains the
        uploaded file path.
        """
        return "%s-path" % name

    def value_from_datadict(self, data, files, name):
        filename = data.get(self.path_input_hidden_name(name))
        storage = self.storage
        if filename is not None and len(filename) > 0 \
                and storage.exists(filename):
            file = storage.open(filename)
            return UploadedFile(
                file=file,
                name = filename,
                content_type=guess_type(file.name)[0],
                size = storage.size(filename)
            )
        return files.get(name, None)

    @property
    def storage(self):
        return FileSystemStorage(location=self.chunks_dir)
