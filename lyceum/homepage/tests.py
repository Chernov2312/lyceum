from http import HTTPStatus

import django.test


class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = django.test.Client().get('/coffee/')
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)


class ReversedTests(django.test.TestCase):
    ...
    # def test_coffee_content(self):
    #     response = self.client.get('/coffee/')
    #     self.assertIn('Я чайник', response.content.decode())
