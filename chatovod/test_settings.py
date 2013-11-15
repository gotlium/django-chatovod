# -*- coding: utf-8 -*-

import os

from django import VERSION

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

DATABASE_ENGINE = 'sqlite3'

SITE_ID = 1

SECRET_KEY = 'cb452188a1c017e94f96d9f813ec2bf8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'chatovod',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_ROOT = '%s/../demo/demo/templates' % PROJECT_ROOT
TEMPLATE_DIRS = (TEMPLATE_ROOT,)

ROOT_URLCONF = 'chatovod.test_urls'

if VERSION[:2] < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)
