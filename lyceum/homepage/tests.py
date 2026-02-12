from http import HTTPStatus

import django.test
from django.test import Client, override_settings

from lyceum.middleware import ReverseRussianMiddleware


class StaticURLTestsTestCase(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get('/coffee/')
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)


class ReversedCoffeeTests(django.test.TestCase):
    def setUp(self):
        self.client = Client()
        ReverseRussianMiddleware.counter = 0

    @override_settings(ALLOW_REVERSE=True)
    def test_coffee_reverse_content_true(self):
        for _ in range(10):
            response = self.client.get('/coffee/')
        self.assertIn('Я кинйач', response.content.decode())

    @override_settings(ALLOW_REVERSE=False)
    def test_coffee_reverse_content_false(self):
        for _ in range(10):
            response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())

    @override_settings(ALLOW_REVERSE=True)
    def test_coffee_content(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())

    @override_settings(ALLOW_REVERSE=True)
    def test_new_clients_content(self):
        for _ in range(10):
            response = self.client.get('/coffee/')
            self.client = Client()
        self.assertIn('Я кинйач', response.content.decode())
