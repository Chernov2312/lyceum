from django.test import Client, TestCase, override_settings


class ReversedCoffeeTests(TestCase):
    def setUp(self):
        self.client = Client()

    @override_settings(ALLOW_REVERSE=True)
    def test_coffee__reverse_content_true(self):
        for _ in range(10):
            response = self.client.get('/coffee/')
        self.assertIn('Я кинйач', response.content.decode())

    @override_settings(ALLOW_REVERSE=False)
    def test_coffee__reverse_content_false(self):
        for _ in range(10):
            response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())

    @override_settings(ALLOW_REVERSE=True)
    def test_coffee_content(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())
