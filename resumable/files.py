# -*- coding: utf-8 -*-
import fnmatch


class ResumableFile(object):
    def __init__(self, storage, kwargs):
        self.storage = storage
        self.kwargs = kwargs
        self.chunk_suffix = "_part_"

    @property
    def chunk_exists(self):
        """Checks if the requested chunk exists."""
        name = "%s%s%s" % (self.filename,
                           self.chunk_suffix,
                           self.kwargs.get('resumableChunkNumber').zfill(4))
        if not self.storage.exists(name):
            return False
        chunk_size = int(self.kwargs.get('resumableCurrentChunkSize'))
        return self.storage.size(name) == chunk_size

    def chunk_names(self):
        """Iterates over all stored chunks and yields their names."""
        file_names = sorted(self.storage.listdir('')[1])
        pattern = '%s%s*' % (self.filename, self.chunk_suffix)
        for name in file_names:
            if fnmatch.fnmatch(name, pattern):
                yield name

    def chunks(self):
        """Yield the contents of every chunk, FileSystemStorage.save compatible
        """
        for name in self.chunk_names():
            yield self.storage.open(name).read()

    def delete_chunks(self):
        [self.storage.delete(chunk) for chunk in self.chunk_names()]

    @property
    def filename(self):
        """Gets the filename."""
        filename = self.kwargs.get('resumableFilename')
        if '/' in filename:
            raise Exception('Invalid filename')
        return "%s_%s" % (
            self.kwargs.get('resumableTotalSize'),
            filename
        )

    @property
    def is_complete(self):
        """Checks if all chunks are allready stored."""
        if self.storage.exists(self.filename):
            return True
        return int(self.kwargs.get('resumableTotalSize')) == self.size

    def process_chunk(self, file):
        if not self.chunk_exists:
            self.storage.save('%s%s%s' % (
                self.filename,
                self.chunk_suffix,
                self.kwargs.get('resumableChunkNumber').zfill(4)
            ), file)

    @property
    def size(self):
        """Gets chunks size."""
        size = 0
        for chunk in self.chunk_names():
            size += self.storage.size(chunk)
        return size
