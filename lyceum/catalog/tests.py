import django.test


class StaticURLTests(django.test.TestCase):
    def test_item_list_endpoint(self):
        response = django.test.Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        response = django.test.Client().get('/catalog/52/')
        self.assertEqual(response.status_code, 200)
