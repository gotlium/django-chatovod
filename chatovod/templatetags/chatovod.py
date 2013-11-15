# -*- coding: utf-8 -*-

from urllib import urlencode
from hashlib import md5

from django import template

import defaults


register = template.Library()


@register.inclusion_tag('chatovod/chat.html', takes_context=True)
def chatovod(context):
    request = context.get('request')
    if request and request.user.is_authenticated() and defaults.CHAT_API_KEY:
        auth_hash = u'%s%s%s' % (
            request.user.username, request.user.email, defaults.CHAT_API_KEY)
        query = {
            'akey': md5(auth_hash.encode('utf8')).hexdigest(),
            'anick': request.user.username.encode('utf8'),
            'aemail': request.user.email,
            'amode': defaults.CHAT_MODE,
        }
        query.update(defaults.CHAT_QUERY)
    else:
        query = defaults.CHAT_QUERY

    if defaults.CHAT_TYPE == 'iframe':
        chat_url = 'http://%s/widget/?%s'
    else:
        chat_url = 'http://%s/widget.js?%s'

    return {
        'type': defaults.CHAT_TYPE,
        'width': defaults.CHAT_WIDTH,
        'height': defaults.CHAT_HEIGHT,
        'divId': defaults.CHAT_ASYNC_DIV_ID,
        'chat_url': chat_url % (defaults.CHAT_DOMAIN, urlencode(query)),
    }
