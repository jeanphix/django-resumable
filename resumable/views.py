# -*- coding: utf-8 -*-
from django.conf import settings

from django.views.generic import View
from django.http import Http404, HttpResponse
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage

from resumable.files import ResumableFile


class ResumableUploadView(View):
    def get(self, *args, **kwargs):
        """Checks if chunk has allready been sended.
        """
        r = ResumableFile(self.storage, self.request.GET)
        if not r.chunk_exists:
            return HttpResponse('chunk not found', status=404)
        return HttpResponse('chunk already exists')

    def post(self, *args, **kwargs):
        """Saves chunks then checks if the file is complete.
        """
        chunk = self.request.FILES.get('file')
        r = ResumableFile(self.storage, self.request.POST)
        if r.chunk_exists:
            return HttpResponse('chunk already exists')
        r.process_chunk(chunk)
        if r.is_complete:
            self.process_file(r.filename, r.file)
            r.delete_chunks()
        return HttpResponse()

    def process_file(self, filename, file):
        """Process the complete file.
        """
        self.storage.save(filename, file)

    @property
    def storage(self):
        chunks_root = getattr(settings, 'CHUNKS_ROOT', None)
        if chunks_root is None:
            raise ImproperlyConfigured('You must set a CHUNKS_ROOT setting')
        return FileSystemStorage(location=chunks_root)
