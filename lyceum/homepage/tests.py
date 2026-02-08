import django.test


class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = django.test.Client().get('/coffee/')
        self.assertEqual(response.status_code, 418)

    def test_coffee_content(self):
        response = self.client.get('/coffee/')
        self.assertEqual(response.content.decode(), 'Я чайник')
