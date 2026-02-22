from django.conf import settings
import django.test
from django.test import Client, override_settings

from lyceum.middleware import ReverseRussianMiddleware


class ReversedCoffeeTests(django.test.TestCase):
    def setUp(self):
        ReverseRussianMiddleware.counter = 0

    @override_settings(ALLOW_REVERSE=True)
    def test_coffee_reverse_content_true(self):
        for _ in range(settings.REQUESTS_COUNT_BEFORE_REVERSE):
            response = self.client.get('/coffee/')
        self.assertIn('Я кинйач', response.content.decode())

    @override_settings(ALLOW_REVERSE=False)
    def test_coffee_reverse_content_false(self):
        for _ in range(settings.REQUESTS_COUNT_BEFORE_REVERSE):
            response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())

    @override_settings(ALLOW_REVERSE=True)
    def test_coffee_content(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())

    @override_settings(ALLOW_REVERSE=True)
    def test_new_clients_content(self):
        for _ in range(settings.REQUESTS_COUNT_BEFORE_REVERSE):
            response = self.client.get('/coffee/')
            self.client = Client()
        self.assertIn('Я кинйач', response.content.decode())

    def test_new_default_content(self):
        for _ in range(settings.REQUESTS_COUNT_BEFORE_REVERSE):
            response = self.client.get('/coffee/')
            self.client = Client()
        self.assertIn('Я кинйач', response.content.decode())
