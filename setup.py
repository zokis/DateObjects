# coding: utf-8
from setuptools import setup

version = __import__('dateobjects').__version__


setup(
    name='dateobjects',
    version=version,
    description='dateobjects is a helper to manipulate dates.',
    long_description='dateobjects is a helper to manipulate dates.',
    url='https://github.com/zokis/DateObjects/',
    author='Marcelo Fonseca Tambalo',
    author_email='marcelo.zokis@gmail.com',
    license='WTFL',
    packages=['dateobjects'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
