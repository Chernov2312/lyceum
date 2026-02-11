import django.test
from parameterized import parameterized


class StaticURLTests(django.test.TestCase):
    def test_item_list_endpoint(self):
        response = django.test.Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        response = django.test.Client().get('/catalog/1/')
        self.assertEqual(response.status_code, 200)


class StaticConverterTests(django.test.TestCase):
    @parameterized.expand(('01', '010', '52'))
    def test_item_converter_posituv_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, 200)

    @parameterized.expand(('-01', '-010', '-52'))
    def test_item_converter_negative_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, 404)

    @parameterized.expand(('00', '0'))
    def test_item_converter_zero_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, 404)


class StaticReTests(django.test.TestCase):
    @parameterized.expand(('00', '0'))
    def test_item_re_zero_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, 404)

    @parameterized.expand(('-01', '-010', '-52'))
    def test_item_re_negative_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, 404)

    @parameterized.expand(('01', '010', '52'))
    def test_item_re_posituv_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, 200)
