from django.test import Client, TestCase

from lyceum.middleware import MiddlewareCounter


class TestToTest(TestCase):
    def setUp(self):
        self.client = Client()
        MiddlewareCounter.counter = 0

    def test_coffee_2(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())
