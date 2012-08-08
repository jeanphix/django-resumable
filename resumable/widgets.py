# -*- coding: utf-8 -*-
from django.forms.widgets import FileInput


class ResumableFileInput(FileInput):
    def path_input_hidden_name(self, name):
        """Returns the name of the input[type=hidden] that contains the
        uploaded file path.
        """
        return "%s-path" % name

    def value_from_datadict(self, data, files, name):
        filename = data.get(self.path_input_hidden_name(name))
        if filename is not None and len(filename) > 0 \
                and self.storage.exists(filename):
            return self.storage.open(filename)
        return files.get(name, None)
