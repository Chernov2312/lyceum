

import django.test
from django.test import Client

import lyceum.settings

reverse = lyceum.settings.ALLOW_REVERSE


class ReversedCoffeeTests(django.test.TestCase):
    def setUp(self):
        self.client = Client()
        lyceum.settings.ALLOW_REVERSE = reverse

    def test_coffee__reverse_content_true(self):
        lyceum.settings.ALLOW_REVERSE = True
        for _ in range(10):
            response = self.client.get('/coffee/')
        self.assertIn('Я кинйач', response.content.decode())

    def test_coffee__reverse_content_false(self):
        lyceum.settings.ALLOW_REVERSE = False
        for _ in range(10):
            response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())

    def test_coffee_content(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())
