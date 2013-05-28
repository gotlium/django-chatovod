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
    if request.user.is_authenticated():
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
    return {
        'chat_url': 'http://%s/widget.js?%s' % (
            settings.CHAT_DOMAIN, urlencode(query))
    }
