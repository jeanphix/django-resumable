# -*- coding: utf-8 -*-
import os

from tempfile import gettempdir

from django.test import TestCase
from django.core.files.base import File
from django.core.files.storage import FileSystemStorage

from resumable.files import ResumableFile


TESTS_ROOT = os.path.dirname(__file__)


seagull = {
    'resumableTotalSize': '147292',
    'resumableFilename': 'seagull.ogg',
    'resumableChunkNumber': '8',
}


craw = {
    'resumableTotalSize': '49028',
    'resumableFilename': 'craw.ogg',
    'resumableChunkNumber': '4',
}


class ResumableFileTest(TestCase):
    def setUp(self):
        test_storage = FileSystemStorage(location='%s/resumable-test' % \
            gettempdir())
        fixtures_root = os.path.join(TESTS_ROOT, 'fixtures', 'files')
        fixtures_storage = FileSystemStorage(location=fixtures_root)

        for filename in fixtures_storage.listdir('.')[1]:
            test_storage.save(
                filename,
                fixtures_storage.open(filename)
            )
        self.seagull = ResumableFile(test_storage, seagull)
        self.craw = ResumableFile(test_storage, craw)
        self.storage = test_storage

    def tearDown(self):
        for filename in self.storage.listdir('.')[1]:
            self.storage.delete(filename)

    def test_chunks(self):
        self.assertEqual(len(self.seagull.chunks), 7)

    def test_chunk_exists_existing(self):
        self.assertTrue(self.craw.chunk_exists)

    def test_chunk_exists_missing(self):
        self.assertFalse(self.seagull.chunk_exists)

    def test_filename(self):
        self.assertEqual(self.seagull.filename, '147292_seagull.ogg')
