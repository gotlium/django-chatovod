# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from chatovod.templatetags import defaults
from django.test.client import Client
from django.test import TestCase


class ChatovodAsyncTestCase(TestCase):
    def _no_auth(self, chat_type=None):
        if chat_type is not None:
            defaults.CHAT_TYPE = chat_type
        client = Client()
        return client.get(reverse("home"))

    def _auth(self, chat_type=None):
        login = 'admin'
        email = 'admin@local.host'
        password = 'password'

        if chat_type is not None:
            defaults.CHAT_TYPE = chat_type

        User.objects.create_superuser(login, email, password)

        client = Client()
        client.login(username=login, password=password)

        return client.get(reverse("home"))

    def _check_auth_params(self, response):
        data_list = [
            'amode=django',
            'anick=admin',
            'width=900',
            'akey=07581c6ee320f0070a2ffabe92aa6550',
            'height=500',
            'aemail=admin%40local.host',
        ]
        for param in data_list:
            self.assertContains(response, param)

    def test_a_async(self):
        response = self._no_auth()
        self.assertContains(response, '<div id="chatovod"></div>')
        self.assertContains(response, '<script type="text/javascript">')
        self.assertContains(
            response, "'http://demo.chatovod.ru/widget.js?width=900&"
                      "height=500&divId=chatovod'")

    def test_b_iframe(self):
        response = self._no_auth('iframe')
        self.assertContains(response, '<iframe')
        self.assertContains(
            response, '"http://demo.chatovod.ru/widget/?width=900&height=500"')

    def test_c_script(self):
        response = self._no_auth('script')
        self.assertContains(response, '<script')
        self.assertContains(
            response,
            '"http://demo.chatovod.ru/widget.js?width=900&height=500"')

    def test_d_async(self):
        response = self._auth('async')
        self.assertContains(response, '<div id="chatovod"></div>')
        self.assertContains(response, '<script type="text/javascript">')
        self._check_auth_params(response)

    def test_e_iframe(self):
        response = self._auth('iframe')
        self.assertContains(response, '<iframe')
        self._check_auth_params(response)

    def test_f_script(self):
        response = self._auth('script')
        self.assertContains(response, '<script')
        self._check_auth_params(response)
