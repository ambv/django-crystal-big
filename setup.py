# -*- encoding: utf-8 -*-
# Copyright (C) 2010 LangaCore
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import with_statement

import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as ld_file:
    long_description = ld_file.read()

setup (
    name = 'django-crystal-big',
    version = '2011.20.10',
    author = 'Everaldo Coehlo, Lukasz Langa',
    author_email = 'contact@everaldo.com, lukasz@langa.pl',
    description = "Everaldo's Crystal icons (big sizes) bundled for direct consumption "
                  "from Django applications",
    long_description = long_description,
    url = 'http://www.everaldo.com/crystal/',
    keywords = 'django big crystal icons everaldo lgpl static',
    platforms = ['any'],
    license = 'LGPL',
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    zip_safe = False, # because executing support extensions for settings.py
                      # requires actual files
    install_requires = [
        'django>=1.2',
        ],

    classifiers = [
        'Development Status :: 6 - Mature',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
