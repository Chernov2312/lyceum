from http import HTTPStatus

import django.test


class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = django.test.Client().get('/coffee/')
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)


class ReversedCoffeeTests(django.test.TestCase):
    def test_coffee__reverse_content(self):
        from lyceum.settings import ALLOW_REVERSE

        if ALLOW_REVERSE:
            for _ in range(10):
                response = self.client.get('/coffee/')
            self.assertIn('Я кинйач', response.content.decode())
        else:
            response = self.client.get('/coffee/')
            self.assertIn('Я чайник', response.content.decode())

    def test_coffee_content(self):
        response = self.client.get('/coffee/')
        self.assertIn('Я чайник', response.content.decode())
