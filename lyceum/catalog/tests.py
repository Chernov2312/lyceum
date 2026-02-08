import django.test


class StaticURLTests(django.test.TestCase):
    def test_item_list_endpoint(self):
        response = django.test.Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        response = django.test.Client().get('/catalog/52/')
        self.assertEqual(response.status_code, 200)

    def test_item_converter_posituv_digit_endpoint(self):
        response = django.test.Client().get('/catalog/converter/52/')
        self.assertEqual(response.status_code, 200)

    def test_item_converter_negative_digit_endpoint(self):
        response = django.test.Client().get('/catalog/converter/-42/')
        self.assertEqual(response.status_code, 404)

    def test_item_converter_zero_endpoint(self):
        response = django.test.Client().get('/catalog/converter/0/')
        self.assertEqual(response.status_code, 404)

    def test_item_re_posituv_digit_endpoint(self):
        response = django.test.Client().get('/catalog/re/52/')
        self.assertEqual(response.status_code, 200)

    def test_item_re_negative_digit_endpoint(self):
        response = django.test.Client().get('/catalog/re/-52/')
        self.assertEqual(response.status_code, 404)

    def test_item_re_zero_endpoint(self):
        response = django.test.Client().get('/catalog/re/0/')
        self.assertEqual(response.status_code, 404)

    def test_item_re_zero2_endpoint(self):
        response = django.test.Client().get('/catalog/re/00/')
        self.assertEqual(response.status_code, 404)
