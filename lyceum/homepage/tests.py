import http

import django.test
from django.test import Client


class StaticURLTestsTestCase(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_coffee_endpoint_status_code(self):
        response = Client().get('/coffee/')
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)

    def test_coffee_endpoint_content(self):
        response = Client().get('/coffee/')
        self.assertEqual(response.content.decode('utf-8'), 'Я — чайник')

    def test_coffee_endpoint_content_type(self):
        response = Client().get('/coffee/')
        self.assertEqual(response['Content-Type'], 'text/plain; charset=utf-8')
