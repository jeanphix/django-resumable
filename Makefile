test:
	- export PYTHON_PATH=. && `which django-admin.py` test resumable --settings=resumable.tests.settings
