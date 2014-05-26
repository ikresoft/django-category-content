#!/usr/bin/env python

from setuptools import setup, find_packages
github_url = 'https://github.com/ikresoft/django-category-content'


setup(
    name='django-category-content',
    version='1.0',
    description='Django category content',
    long_description='Django category content',
    author='Enver Bisevac, Mirza Delic',
    author_email='ikresoft@gmail.com',
    url=github_url,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django, Django Base Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
)
