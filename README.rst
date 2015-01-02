django-resumable
----------------

.. image:: https://drone.io/github.com/jeanphix/django-resumable/status.png
   :target: https://drone.io/github.com/jeanphix/django-resumable/latest

``django-resumable`` provides django backend stuff that handles `resumable.js <https://github.com/23/Resumable.js>`_ xhr uploads.



Installation
------------

* ``pip install django-resumable``
* Add ``resumable`` to your ``INSTALLED_APPS``


Views
-----

In order to upload files asynchronous, you must define an endpoint that will deal
with uploaded file chunks:

.. code-block:: python

    from django.contrib.auth.decorators import login_required

    from resumable.views import ResumableUploadView


    urlpatterns += patterns('',
        url('^upload/$', login_required(ResumableUploadView.as_view()),
            name='upload'),
    )

You should also consider having per user chunk upload directory:

.. code-block:: python

    class MyResumableUploadView(ResumableUploadView):
        @property
        def chunks_dir(self):
            return self.request.user.profile.chunks_dir


Fields
------

If you want to handle resumable upload within your forms, you can use the ``ResumableFileField``
that works like django core ``FileField``:

.. code-block:: python

    from django.conf import settings
    from django.core.urlresolvers import reverse

    from resumable.fields import ResumableFileField


    class ResumableForm(Form):
        file = ResumableFileField(
            allowed_mimes=("audio/ogg",),
            upload_url=lambda: reverse('upload'),
            chunks_dir=getattr(settings, 'FILE_UPLOAD_TEMP_DIR')
        )


Javascript
----------

``django-resumable`` comes with extendable frontend scripts that work out of the box:

.. code-block:: html

    {% load staticfiles %}
    <!DOCTYPE html>
    <html>
        <body>
            <form method="post" action=".">
                <fieldset>
                    {% csrf_token %}
                    {{ form.as_p }}
                </fieldset>
                <p><input type="submit" value="send" /></p>
            </form>
            <script type="text/javascript" src="https://raw.github.com/23/resumable.js/master/resumable.js"></script>
            <script type="text/javascript" src="{% static 'resumable/js/django-resumable.js' %}"></script>
            <script type="text/javascript" src="{% static 'resumable/js/init.js' %}"></script>
        </body>
    </html>
