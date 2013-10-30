Chatovod - chat widget for Django
=================================

What's that
-----------
This reusable Django app will be integrate a chat widget from Chatovod.Ru


Installation:
-------------
1. Package:

.. code-block:: bash

    $ git clone https://github.com/gotlium/django-chatovod.git

    $ cd django-chatovod && sudo python setup.py install

**OR**

.. code-block:: bash

    $  sudo pip install django-chatovod


2. Add the ``chatovod`` application to ``INSTALLED_APPS`` in your settings file (usually ``settings.py``)

3. Configure widget on your settings. By default:

.. code-block:: python

    CHAT_WIDTH = '900'
    CHAT_HEIGHT = '500'
    CHAT_DOMAIN = 'dletest.chatovod.ru'
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


.. image:: https://d2weczhvl823v0.cloudfront.net/gotlium/django-chatovod/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

