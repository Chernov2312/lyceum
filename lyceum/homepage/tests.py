from django.test import Client, TestCase

from lyceum.middleware import MiddlewareCounter


class TestToTest(TestCase):
    def setUp(self):
        self.client = Client()
        MiddlewareCounter.counter = 0

    def test_coffee__reverse_content_true(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())
