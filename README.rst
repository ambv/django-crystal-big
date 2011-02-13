------------------
django-crystal-big
------------------

This library bundles `Everaldo's Crystal icons
<http://www.everaldo.com/crystal/>`_ for direct consumption with Django
applications. Sizes available are 64x64 and 128x128. Look for
`django-crystal-small <http://pypi.python.org/pypi/django-crystal-small/>`_ for
16x16, 22x22, 24x24, 32x32 and 48x48.

Very simple installation:

* Use Django 1.3 or `django-staticfiles
  <http://pypi.python.org/pypi/django-staticfiles/>`_
  
* add ``django_crystal_big`` to ``INSTALLED_APPS``
  
* run ``manage.py collectstatic`` should pick up Crystal icons as well. They are
  available under the ``crystal`` directory

The latest version can be installed via `PyPI
<http://pypi.python.org/pypi/django-crystal-big/>`_::

  $ pip install django-crystal-big
  
or::

  $ easy_install django-crystal-big

The `source code repository <http://github.com/LangaCore/django-crystal-big>`_
and `issue tracker <http://github.com/LangaCore/django-crystal-big/issues>`_ are
maintained on `GitHub <http://github.com/LangaCore/django-crystal-big>`_.

**Note:** This is only a handy Django-specific bundle of icons originally
crafted by `Everaldo Coelho <http://www.everaldo.com/about/>`_ and contributors.
These icons have been released under the LGPL, and so is this bundle.
