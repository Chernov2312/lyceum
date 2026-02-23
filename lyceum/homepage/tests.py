import http

import django.test
from django.test import Client
from django.test import override_settings
from django.urls import reverse

__all__ = ['StaticTeaURLTestCase']


@override_settings(ALLOW_REVERSE=False)
class StaticTeaURLTestCase(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = Client().get(reverse('main:home'))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_coffee_endpoint_status_code(self):
        response = Client().get(reverse('main:coffee'))
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)
        self.assertEqual(response.content.decode('utf-8'), 'Я чайник')
