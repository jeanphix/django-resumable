# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-resumable',
    version='0.2.0-dev',
    author=u'jean-philippe serafin',
    author_email='serafinjp@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/jeanphix/django-resumable',
    license='MIT licence',
    description='Django resumable uploads',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django>=1.9',
        'python-magic',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
