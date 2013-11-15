Installation
============

Recommended way to install is via pip::

  pip install django-chatovod


Basic
-----

* Add ``chatovod`` to ``INSTALLED_APPS`` in settings.py::

    INSTALLED_APPS = (
        ...
        'chatovod',
        ...
    )

* Configure widget on your settings::

    CHAT_WIDTH = '900'
    CHAT_HEIGHT = '500'
    CHAT_DOMAIN = 'demo.chatovod.ru'
    CHAT_API_KEY = '07a128c26a0e626c6afcc5ecd8ed800c'


Compatibility
-------------
* Python: 2.6, 2.7
* Django: 1.3.x, 1.4.x, 1.5.x, 1.6
