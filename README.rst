django-resumable
----------------

``django-resumable`` provides django backend stuff that handles `resumable.js`_ xhr uploads.

.. resumable.js: https://github.com/23/Resumable.js


Installation
------------

* ``pip install django-resumable``
* Add ``resumable`` to your ``INSTALLED_APPS``


Views
-----

In order to upload files asynchronous, you must defined un endpoint that will deals
with uploaded file chunks.::

    from django.contrib.auth.decorators import login_required

    from resumable.views import ResumableUploadView


    urlpatterns += patterns('',
        url(^upload/$', login_required(ResumableUploadView.as_view()),
            name='upload'),
    )

You should also consider having per user chunk upload directory.::

    class MyResumableUploadView(ResumableUploadView):
        @property
        def chuns_dir(self):
            return request.user.profile.chunks_dir


Fields
------

If you want to handle resumable upload within your forms, you can use the ``ResumableFileField``
that works like django core ``FileField``.::

    from django.conf import settings
    from django.core.urlresolvers import reverse

    from resumable.fields import ResumableFileField


    class ResumableForm(Form):
        file = ResumableFileField(
            allowed_mimes=("audio/ogg",),
            upload_url=lambda: reverse('upload'),
            chunks_dir=getattr(settings, 'FILE_UPLOAD_TEMP_DIR')
        )
