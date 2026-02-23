import http

import django.test
from django.urls import reverse

__all__ = ['StaticURLTests']


class StaticURLTests(django.test.TestCase):
    def test_description_endpoint(self):
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
