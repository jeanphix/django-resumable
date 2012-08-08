test:
	- export PYTHON_PATH=`pwd` && `which django-admin.py` test resumable --settings=resumable.tests.settings
