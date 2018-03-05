Chatovod - chat widget for Django
=================================

What's that
-----------
This reusable Django app will be integrate a chat widget from Chatovod.Ru


.. image:: https://api.travis-ci.org/gotlium/django-chatovod.png?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/gotlium/django-chatovod
.. image:: https://coveralls.io/repos/gotlium/django-chatovod/badge.png?branch=master
    :target: https://coveralls.io/r/gotlium/django-chatovod?branch=master
.. image:: https://img.shields.io/pypi/v/django-chatovod.svg
    :alt: Current version on PyPi
    :target: https://crate.io/packages/django-chatovod/
.. image:: https://img.shields.io/pypi/dm/django-chatovod.svg
    :alt: Downloads from PyPi
    :target: https://crate.io/packages/django-chatovod/

Documentation available at `Read the Docs <http://django-chatovod.readthedocs.org/>`_.


Installation:
-------------
1. Package:

.. code-block:: bash

    $ git clone https://github.com/gotlium/django-chatovod.git

    $ cd django-chatovod && sudo python setup.py install

**OR**

.. code-block:: bash

    $  pip install django-chatovod


2. Add the ``chatovod`` application to ``INSTALLED_APPS`` in your settings file (usually ``settings.py``)

3. Configure widget on your settings. By default:

.. code-block:: python

    CHAT_WIDTH = '900'
    CHAT_HEIGHT = '500'
    CHAT_DOMAIN = 'demo.chatovod.ru'
    CHAT_API_KEY = '07a128c26a0e626c6afcc5ecd8ed800c'

4. Use in your template:

.. code-block:: html

    {% load chatovod %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chatovod example</title>
    </head>
    <body>
        {% chatovod %}
    </body>
    </html>


Compatibility:
-------------
* Python: 2.6, 2.7
* Django: 1.3.x, 1.4.x, 1.5.x, 1.6


.. image:: https://d2weczhvl823v0.cloudfront.net/gotlium/django-chatovod/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free
