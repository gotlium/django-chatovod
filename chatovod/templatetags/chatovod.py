# -*- coding: utf-8 -*-

from urllib import urlencode
from hashlib import md5
from django import template

import settings


register = template.Library()


@register.inclusion_tag('chatovod/chat.html', takes_context=True)
def chatovod(context):
    if 'request' not in context:
        return
    request = context['request']
    if request.user.is_authenticated() and settings.CHAT_API_KEY:
        auth_hash = u'%s%s%s' % (request.user.username, request.user.email,
                                 settings.CHAT_API_KEY)
        query = {
            'anick': request.user.username.encode('utf8'),
            'aemail': request.user.email,
            'amode': 'django',
            'akey': md5(auth_hash.encode('utf8')).hexdigest()
        }
        query.update(settings.CHAT_QUERY)
    else:
        query = settings.CHAT_QUERY

    js_url = 'http://%s/widget.js?%s' % (
        settings.CHAT_DOMAIN, urlencode(query))
    frame_url = 'http://%s/widget/?%s' % (
        settings.CHAT_DOMAIN, urlencode(query))

    return {
        'chat_url': frame_url if settings.CHAT_TYPE == 'iframe' else js_url,
        'type': settings.CHAT_TYPE,
        'width': settings.CHAT_WIDTH,
        'height': settings.CHAT_HEIGHT,
    }
