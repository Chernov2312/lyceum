import http

from catalog.models import Category, Item, Tag
from catalog.validators import validate_words_in_text

import django.test
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

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
        ('i am venom', 'i am the atomic', '2ab', 'a2b', 'ab2'),
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
        ('i am venom', 'i am the atomic', '2ab', 'a2b', 'ab2'),
    )
    def test_item_re_str_endpoint(self, value):
        response = django.test.Client().get(f'/catalog/re/{value}/')
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)


class ItemModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category',
            weight=100,
        )
        self.tag = Tag.objects.create(name='Тестовый тег', slug='test-tag')

    def test_item_creation_valid_text(self):
        item = Item.objects.create(
            name='Тестовый товар',
            text='превосходно',
            category=self.category,
        )
        item.tags.add(self.tag)

        self.assertEqual(item.name, 'Тестовый товар')
        self.assertTrue(item.is_published)
        self.assertEqual(item.category, self.category)
        self.assertEqual(item.tags.count(), 1)

    @parameterized.expand(
        [
            ('excellent_word', 'Это превосходно работает'),
            ('luxury_word', 'Это роскошно выглядит'),
            ('both_words', 'Это превосходно и роскошно одновременно'),
            ('uppercase_excellent', 'ПРЕВОСХОДНО!'),
            ('uppercase_luxury', 'РОСКОШНО!'),
            ('mixed_case', 'Превосходно и Роскошно'),
        ],
    )
    def test_item_validation_need_wotd_text(self, name, text):
        try:
            validate_words_in_text(text)
        except ValidationError:
            self.fail(f'not nedded word in "{text}"')

    @parameterized.expand(
        [
            ('no_required_words', 'Это обычный текст без нужных слов'),
            ('empty_string', ''),
        ],
    )
    def test_item_validation_not_word(self, name, text):
        with self.assertRaises(ValidationError):
            validate_words_in_text(text)


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(
            name='Электроника',
            slug='electronics',
            weight=100,
        )
        self.assertEqual(category.name, 'Электроника')
        self.assertEqual(category.slug, 'electronics')
        self.assertEqual(category.weight, 100)
        self.assertTrue(category.is_published)

    @parameterized.expand(
        [
            ('min_value', 0),
            ('max_value', 32768),
            ('negative_value', -10),
        ],
    )
    def test_category_weight_invalid_values(self, name, weight):
        category = Category(name='Тест', slug='test', weight=weight)
        with self.assertRaises(ValidationError):
            category.full_clean()

    @parameterized.expand(
        [
            ('default_value', 100),
            ('min', 1),
            ('max', 32767),
        ],
    )
    def test_category_weight_valid_values(self, name, weight):
        category = Category(name='Тест', slug='test', weight=weight)
        try:
            category.full_clean()
        except ValidationError:
            self.fail(f'Category with weight={weight} should be valid!')

    @parameterized.expand(
        [
            ('valid_slug_1', 'test'),
            ('valid_slug_2', 'Test123'),
            ('valid_slug_3', 'a' * 200),
        ],
    )
    def test_category_slug_valid_values(self, name, slug):
        try:
            category = Category.objects.create(
                name='Электроника',
                slug=slug,
                weight=100,
            )
            category.full_clean()
        except ValidationError:
            self.fail(f"Slug '{slug}' should be valid!")

    def test_category_unique_slug(self):
        Category.objects.create(
            name='Категория 1',
            slug='test-slug',
            weight=100,
        )

        with self.assertRaises(IntegrityError):
            Category.objects.create(
                name='Категория 2',
                slug='test-slug',
                weight=200,
            )

    def test_category_str_method(self):
        category = Category.objects.create(
            name='Электроника',
            slug='electronics',
            weight=100,
        )
        self.assertEqual(str(category), 'Электроника')


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name='Новинка', slug='new')
        self.assertEqual(tag.name, 'Новинка')
        self.assertEqual(tag.slug, 'new')
        self.assertTrue(tag.is_published)

    @parameterized.expand(
        [
            ('valid_slug_1', 'new'),
            ('valid_slug_2', 'new_2024'),
            ('valid_slug_3', 'a' * 200),
        ],
    )
    def test_tag_slug_valid_values(self, name, slug):
        tag = Tag(name='Тест', slug=slug)
        try:
            tag.full_clean()
        except ValidationError:
            self.fail(f"Slug '{slug}' should be valid!")

    def test_tag_unique_slug(self):
        Tag.objects.create(name='Тег 1', slug='test-tag')

        with self.assertRaises(IntegrityError):
            Tag.objects.create(name='Тег 2', slug='test-tag')

    def test_tag_str_method(self):
        tag = Tag.objects.create(name='Новинка', slug='new')
        self.assertEqual(str(tag), 'Новинка')


class ItemRelationsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Электроника',
            slug='electronics',
            weight=100,
        )
        self.tag1 = Tag.objects.create(name='Тег 1', slug='tag1')
        self.tag2 = Tag.objects.create(name='Тег 2', slug='tag2')

    def test_item_category_relation(self):
        item = Item.objects.create(
            name='Телефон',
            text='Работает превосходно',
            category=self.category,
        )
        self.assertEqual(item.category, self.category)
        self.assertIn(item, self.category.items.all())

    @parameterized.expand(
        [
            ('one_tag', [1]),
            ('two_tags', [1, 2]),
        ],
    )
    def test_item_tags_relation(self, name, tag_indices):
        item = Item.objects.create(
            name='Телефон',
            text='Работает превосходно',
            category=self.category,
        )

        tags = [self.tag1, self.tag2]
        selected_tags = [tags[i - 1] for i in tag_indices]
        item.tags.add(*selected_tags)

        self.assertEqual(item.tags.count(), len(tag_indices))
        for tag in selected_tags:
            self.assertIn(tag, item.tags.all())
            self.assertIn(item, tag.items.all())
