# -*- coding: utf-8 -*-
import magic

from django.forms.widgets import FileInput, HiddenInput
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from django.utils.safestring import mark_safe
from django.template import loader


class ResumableFileInput(FileInput):
    template_name = 'resumable/file_input.html'

    def __init__(self, *args, **kwargs):
        super(ResumableFileInput, self).__init__(*args, **kwargs)
        self.filepath = None
        self.filename = None

    def filename_input_name(self, name):
        """Returns the name of the input[type=hidden] that contains the
        uploaded file path
        """
        return "%s-path" % name

    def guess_type(self, path):
        mime = magic.Magic(mime=True)
        return mime.from_file(path)

    def value_from_datadict(self, data, files, name):
        filepath = data.get(self.filename_input_name(name))
        storage = self.storage
        if filepath is not None and len(filepath) > 0 \
                and storage.exists(filepath):
            file = storage.open(filepath)
            size = storage.size(filepath)
            self.filepath = filepath
            self.filename = filepath.lstrip('%s_' % unicode(size))
            return UploadedFile(
                file=file,
                name = self.filename,
                content_type=self.guess_type(file.name),
                size = size
            )
        return files.get(name, None)

    def render(self, name, value, attrs=None, **kwargs):
        context = {
            'filename': self.filename,
            'filename_input_value': self.filepath,
            'filename_input_name': self.filename_input_name(name),
            'file_input_name': name,
            'attrs': self.build_attrs(attrs)
        }
        return loader.render_to_string(self.template_name, context)

    @property
    def storage(self):
        return FileSystemStorage(location=self.chunks_dir)
