test:
	- `which django-admin.py` test resumable --settings=resumable.tests.settings --pythonpath=.

testserver:
	- `which django-admin.py` runserver --settings=resumable.tests.settings --pythonpath=.
