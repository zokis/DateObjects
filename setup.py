# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='date-objects',
      version='1.0',
      description='helper for manipulating dates.',
      long_description=open(README).read(),
      author="Marcelo Fonseca Tambalo", author_email="marcelo.zokis@gmail.com",
      py_modules=['DateObjects'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Framework :: Flask',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      url='https://github.com/zokis/DateObjects/',)
