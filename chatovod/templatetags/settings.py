# -*- coding: utf-8 -*-

from django.conf import settings

CHAT_WIDTH = getattr(settings, 'CHAT_WIDTH', '900')
CHAT_HEIGHT = getattr(settings, 'CHAT_HEIGHT', '500')
CHAT_DOMAIN = getattr(settings, 'CHAT_DOMAIN', 'dletest.chatovod.ru')
CHAT_API_KEY = getattr(
    settings, 'CHAT_API_KEY', '07a128c26a0e626c6afcc5ecd8ed800c')

query = {
    'width': CHAT_WIDTH,
    'height': CHAT_HEIGHT
}

CHAT_QUERY = getattr(settings, 'CHAT_QUERY', query)

# async, iframe or none
CHAT_TYPE = getattr(settings, 'CHAT_TYPE', 'async')
