import http

import django.test
from parameterized import parameterized


class StaticURLTests(django.test.TestCase):
    def test_item_list_endpoint(self):
        response = django.test.Client().get('/catalog/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.expand(('01', '010', '52'))
    def test_item_detail_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)


class StaticConverterTests(django.test.TestCase):
    @parameterized.expand(('01', '010', '52'))
    def test_item_converter_posituv_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.expand(('-01', '-010', '-52'))
    def test_item_converter_negative_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    @parameterized.expand(('00', '0'))
    def test_item_converter_zero_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    @parameterized.expand(('0.1', '0.10', '5.2'))
    def test_item_converter_float_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    @parameterized.expand(
        ('i am venom', 'i am the atomic', '2ab', 'a2b', 'ab2')
    )
    def test_item_converter_str_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/converter/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)


class StaticReTests(django.test.TestCase):
    @parameterized.expand(('01', '010', '52'))
    def test_item_re_posituv_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.expand(('-01', '-010', '-52'))
    def test_item_re_negative_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    @parameterized.expand(('00', '0'))
    def test_item_re_zero_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    @parameterized.expand(('0.1', '0.10', '5.2'))
    def test_item_re_float_digit_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)

    @parameterized.expand(
        ('i am venom', 'i am the atomic', '2ab', 'a2b', 'ab2')
    )
    def test_item_re_str_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
