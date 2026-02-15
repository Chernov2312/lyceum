import http

import django.test
from django.test import Client


class StaticURLTestsTestCase(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_coffee_endpoint(self):
        response = Client().get('/coffee/')
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)
