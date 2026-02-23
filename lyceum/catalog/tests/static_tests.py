import http

import django.test
from django.test import override_settings
from django.urls import reverse
from parameterized import parameterized


@override_settings(ALLOW_REVERSE=False)
class StaticURLTests(django.test.TestCase):
    def test_item_list_endpoint(self):
        response = django.test.Client().get(reverse('catalog:item_list'))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.expand(('01', '010', '52'))
    def test_item_detail_endpoint(self, value):
        response = django.test.Client().get(
            reverse('catalog:item_detail', args=[value]),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)


@override_settings(ALLOW_REVERSE=False)
class StaticReTests(django.test.TestCase):
    @parameterized.expand(('01', '010', '52'))
    def test_item_re_posituv_digit_endpoint(self, value):
        response = django.test.Client().get(
            reverse('catalog:re_item_detail', args=[value]),
        )
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    @parameterized.expand(
        (
            'i am venom',
            'i am the atomic',
            '2ab',
            'a2b',
            'ab2',
            '0',
            '00',
            '-1',
            '-42',
            '-100500',
            '--1',
            '-0',
            '--0',
            '0.1',
            '1.5',
            '3.14',
            '.5',
            '5.',
            '-0.1',
            '-1.5',
            '0,1',
            '1,5',
            '-0.1',
            '-1.5',
            '-3.14',
            '-.5',
            '-5.',
            '+1',
            '+42',
            '+100500',
            '+0',
            '+01',
            '+010',
            '',
            '//',
            'abc',
            'hello-world',
            'test123',
            '123test',
            'привет',
            'テスト',
            'اختبار',
            '😀',
            '🔥',
            '👨‍💻',
            '🚀',
            '❤️',
            '👍🏼',
            '中',
            '国',
            '日本',
            '漢字',
            '中文',
            '中國',
            '१',
            '१२',
            '१२३',
            '४५६',
            '७८९',
            '०',
            '১',
            '২',
            '৩',
            '৪',
            '৫',
            '৬',
            '৭',
            '৮',
            '৯',
            '০',
            '1e3',
            '1E3',
            '1e+3',
            '1e-3',
            '1.5e3',
            '1.5E3',
            '1.5e-3',
            '.5e3',
            '5.e3',
            '1e03',
            '1e003',
            '1_000',
            '1_000_000',
            '100_000',
            '1_2_3',
            '1_000_000_000',
            '_100',
            '100_',
            '1__000',
            '123abc456',
            'abc123def',
            '!@#$%',
            '  123  ',
            '１２３',
            '①②③',
            '½',
            '⅓',
            '⅔',
            '¼',
            '¾',
            '∞',
            'NaN',
            'null',
            'undefined',
            'true',
            'false',
        ),
    )
    def test_mixed_invalid_values(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
