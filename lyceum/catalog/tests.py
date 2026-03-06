import http

from django.core.exceptions import ValidationError
from django.db.models import QuerySet
import django.test
from django.test import override_settings
from django.urls import reverse
from parameterized import parameterized

from catalog.models import Category, Item, Tag

__all__ = [
    'CategoryModelTest',
    'ItemModelTest',
    'LengthTest',
    'TagModelTest',
    'UniqueNameTest',
    'StaticURLTests',
    'StaticReTests',
]


@override_settings(ALLOW_REVERSE=False)
class StaticURLTests(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category',
            weight=100,
        )

        cls.tag1 = Tag.objects.create(
            name='asdfghjkl;',
            slug='asdfghjk',
        )
        cls.tag2 = Tag.objects.create(
            name='qwertyu',
            slug='qwerty',
        )
        items_data = [
            (1, 'Товар 1', 'Этот товар просто превосходно!'),
            (10, 'Товар dfghjk10', 'Товар 10 - роскошно выглядит!'),
            (52, 'Товар asdfghjkl52', 'Товар 52 - превосходно выбор!'),
        ]

        for item_id, name, text in items_data:
            item = Item.objects.create(
                id=item_id,
                name=name,
                text=text,
                category=cls.category,
            )
            item.tags.add(cls.tag1, cls.tag2)

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
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category',
            weight=100,
        )

        cls.tag1 = Tag.objects.create(
            name='asdfghjkl;',
            slug='asdfghjk',
        )
        cls.tag2 = Tag.objects.create(
            name='qwertyu',
            slug='qwerty',
        )
        items_data = [
            (1, 'Товар 1', 'Этот товар просто превосходно!'),
            (10, 'Товар dfghjk10', 'Товар 10 - роскошно выглядит!'),
            (52, 'Товар asdfghjkl52', 'Товар 52 - превосходно выбор!'),
        ]

        for item_id, name, text in items_data:
            item = Item.objects.create(
                id=item_id,
                name=name,
                text=text,
                category=cls.category,
            )
            item.tags.add(cls.tag1, cls.tag2)

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


@override_settings(ALLOW_REVERSE=False)
class ItemModelTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Test Category',
            slug='test-category',
        )

    @classmethod
    def tearDownClass(cls):
        cls.category.delete()
        super().tearDownClass()

    @parameterized.expand(
        [
            ('Hgh', True, 'rangom превосходно'),
            ('Another', False, 'ПРевосходно'),
            ('Another', False, 'Роскошно'),
            ('Another', False, 'росКошно'),
        ],
    )
    def test_create_full(self, name, is_published, text):
        count = Item.objects.count()
        item = Item.objects.create(
            name=name,
            is_published=is_published,
            text=text,
            category=self.category,
        )
        self.assertEqual(count + 1, Item.objects.count())
        self.assertEqual(item.name, name)
        self.assertEqual(item.is_published, is_published)
        self.assertEqual(item.text, text)
        self.assertEqual(item.category, self.category)

    @parameterized.expand(
        [
            ('Hgh', True, 'rangom'),
            ('Another', False, 'что-то'),
        ],
    )
    def test_invalid_create(self, name, is_published, text):
        item = Item(
            name=name,
            is_published=is_published,
            text=text,
            category=self.category,
        )
        with self.assertRaises(ValidationError):
            item.full_clean()


@override_settings(ALLOW_REVERSE=False)
class TagModelTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tag = Tag.objects.create(
            name='Test Tag',
            slug='test-tag',
            is_published=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.tag.delete()
        super().tearDownClass()

    def test_create_minimal(self):
        tag_count = Tag.objects.count()
        tag = Tag.objects.create(
            name='Minimal Tag',
            slug='minimal-tag',
        )

        self.assertEqual(tag_count + 1, Tag.objects.count())
        self.assertEqual(tag.name, 'Minimal Tag')
        self.assertEqual(tag.slug, 'minimal-tag')
        self.assertIsNotNone(tag.is_published)

    def test_create_full(self):
        tag_count = Tag.objects.count()
        tag = Tag.objects.create(
            name='Full Tag',
            slug='full-tag',
            is_published=False,
        )

        self.assertEqual(tag_count + 1, Tag.objects.count())
        self.assertEqual(tag.name, 'Full Tag')
        self.assertEqual(tag.slug, 'full-tag')
        self.assertFalse(tag.is_published)

    def test_slug_unique(self):
        Tag.objects.create(
            name='First Tag',
            slug='unique-slug',
        )
        with self.assertRaises(ValidationError):
            Tag.objects.create(
                name='Second Tag',
                slug='unique-slug',
            )

    def test_slug_validation(self):
        tag = Tag(
            name='Invalid Slug Tag',
            slug='некорректный слаг',
        )
        with self.assertRaises(ValidationError):
            tag.full_clean()


@override_settings(ALLOW_REVERSE=False)
class CategoryModelTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Test Category',
            slug='test-category',
            weight=150,
            is_published=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.category.delete()
        super().tearDownClass()

    def test_create_minimal(self):
        category_count = Category.objects.count()
        category = Category.objects.create(
            name='Minimal Category',
            slug='minimal-category',
        )

        self.assertEqual(category_count + 1, Category.objects.count())
        self.assertEqual(category.name, 'Minimal Category')
        self.assertEqual(category.slug, 'minimal-category')
        self.assertEqual(category.weight, 100)
        self.assertIsNotNone(category.is_published)

    def test_create_full(self):
        category_count = Category.objects.count()
        category = Category.objects.create(
            name='Full Category',
            slug='full-category',
            weight=500,
            is_published=False,
        )

        self.assertEqual(category_count + 1, Category.objects.count())
        self.assertEqual(category.name, 'Full Category')
        self.assertEqual(category.slug, 'full-category')
        self.assertEqual(category.weight, 500)
        self.assertFalse(category.is_published)

    @parameterized.expand((0, 32768))
    def test_weight_validation(self, weight):
        category = Category(
            name='Min Weight Category',
            slug='min-weight',
            weight=weight,
        )

        with self.assertRaises(ValidationError) as context:
            category.full_clean()

        self.assertIn('weight', context.exception.message_dict)

    @parameterized.expand(
        [
            (1,),
            (100,),
            (32767,),
        ],
    )
    def test_weight_boundary_values(self, weight):
        category = Category(
            name=f'Weight Test {weight}',
            slug=f'weight-{weight}',
            weight=weight,
        )
        category.full_clean()

    @parameterized.expand(('-a'))
    def test_minus_slug(self, slug):
        category = Category(
            name='gg',
            slug=slug,
            weight=1,
        )
        category.full_clean()


@override_settings(ALLOW_REVERSE=False)
class UniqueNameTest(django.test.TestCase):
    @parameterized.expand(
        [
            ('Гений', 'Гений'),
            ('Гений', 'гений'),
            ('Гений', 'ГеHий!'),
            ('Гений', 'Гений '),
            ('гений', 'геееееений'),
            ('Рома', 'Poма'),
            ('Ворон', 'Boрон'),
            ('lol', 'IoI'),
            ('Заря', '3аря'),
        ],
    )
    def test_unique(self, name, test_name, slug='deth'):
        category_1 = Category(
            name=name,
            slug=slug,
        )
        category_1.save()
        category_2 = Category(
            name=test_name,
            slug=slug + '10',
        )
        with self.assertRaises(ValidationError):
            category_2.save()


@override_settings(ALLOW_REVERSE=False)
class LengthTest(django.test.TestCase):
    @parameterized.expand(('a' * 150, 'a'))
    def test_max_min_name_length(self, name):
        category = Category(
            name=name,
            slug='min-weight',
            weight=1,
        )
        category.full_clean()

    @parameterized.expand(('a' * 200, 'a'))
    def test_max_min_slug_length(self, slug):
        category = Category(
            name='gg',
            slug=slug,
            weight=1,
        )
        category.full_clean()


class CatalogContextTests(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category',
            weight=100,
            is_published=True,
        )

        cls.tag = Tag.objects.create(
            name='Тестовый тег',
            slug='test-tag',
            is_published=True,
        )

        cls.item = Item.objects.create(
            name='Тестовый товар',
            text='Это превосходно товар',
            category=cls.category,
            is_published=True,
        )
        cls.item.tags.add(cls.tag)

        cls.item2 = Item.objects.create(
            name='Второй товар',
            text='Роскошно товар',
            category=cls.category,
            is_published=True,
        )
        cls.item2.tags.add(cls.tag)

    def test_item_list_context(self):
        response = django.test.Client().get(reverse('catalog:item_list'))

        self.assertIsNotNone(response.context)

        self.assertIn('items', response.context)

        items = response.context['items']
        self.assertEqual(len(items), 2)
        self.assertIn(self.item, items)
        self.assertIn(self.item2, items)

    def test_item_detail_context(self):
        response = django.test.Client().get(
            reverse('catalog:item_detail', args=[self.item.id]),
        )

        self.assertIsNotNone(response.context)
        self.assertIn('item', response.context)

        item = response.context['item']
        self.assertEqual(item.name, 'Тестовый товар')
        self.assertIn('превосходно', item.text)

        self.assertTrue(item.tags.exists())
        self.assertEqual(item.category.name, 'Тестовая категория')

    def test_item_list_context_contains_only_published(self):
        unpublished_item = Item.objects.create(
            name='Неопубликованный товар',
            text='превосходно',
            category=self.category,
            is_published=False,
        )

        response = django.test.Client().get(reverse('catalog:item_list'))
        items = response.context['items']

        self.assertNotIn(unpublished_item, items)
        self.assertIn(self.item, items)
        self.assertIn(self.item2, items)
        self.assertEqual(items.count(), 2)

    def test_item_list_context_pagination(self):
        response = django.test.Client().get(reverse('catalog:item_list'))
        items = response.context['items']

        from django.db.models.query import QuerySet

        self.assertIsInstance(items, QuerySet)

    def test_item_list_ordering(self):
        response = django.test.Client().get(reverse('catalog:item_list'))
        items = list(response.context['items'])

        item_names = [item.name for item in items]
        self.assertEqual(item_names, sorted(item_names))

    def test_re_item_detail_context(self):
        response = django.test.Client().get(
            reverse('catalog:re_item_detail', args=[str(self.item.id)]),
        )

        self.assertIsNotNone(response.context)
        self.assertIn('item', response.context)

        item = response.context['item']
        self.assertEqual(item.name, 'Тестовый товар')


class ItemManagerGetObjectOr404Test(django.test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name='Категория',
            slug='cat',
            is_published=True,
        )
        cls.item = Item.objects.create(
            name='Товар',
            text='превосходно',
            category=cls.category,
            is_published=True,
        )
        cls.unpublished = Item.objects.create(
            name='Неопубликованный',
            text='превосходно',
            category=cls.category,
            is_published=False,
        )

    @parameterized.expand(
        [
            ('существующий_опубликованный', 'item', True),
            ('несуществующий_id', 999, False),
            ('неопубликованный_товар', 'unpublished', False),
        ],
    )
    def test_get_object_or_404_returns_value(
        self,
        name,
        item_key,
        expected_is_not_none,
    ):
        if item_key == 'item':
            item_id = self.item.id
        elif item_key == 'unpublished':
            item_id = self.unpublished.id
        else:
            item_id = item_key

        result = Item.objects.get_object_or_404(item_id)

        if expected_is_not_none:
            self.assertIsNotNone(result)
            self.assertEqual(result.id, item_id)
        else:
            self.assertIsNone(result)


class CatalogViewsTest(django.test.TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Категория',
            slug='cat',
            is_published=True,
        )
        self.item = Item.objects.create(
            name='Товар',
            text='превосходно',
            category=self.category,
            is_published=True,
        )

    def test_item_list_context_has_items(self):
        response = self.client.get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)

    def test_item_list_context_items_type(self):
        response = self.client.get(reverse('catalog:item_list'))
        self.assertIsInstance(response.context['items'], QuerySet)

    def test_item_list_context_items_count(self):
        response = self.client.get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['items']), 1)

    def test_item_list_items_have_related_category(self):
        response = self.client.get(reverse('catalog:item_list'))
        item = response.context['items'][0]
        self.assertTrue(hasattr(item, 'category'))
        self.assertEqual(item.category.name, 'Категория')


class ContextTests(django.test.TestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.published_category = Category.objects.create(
            is_published=True,
            name='test category 1',
            slug='published_category',
            weight='100',
        )
        cls.unpublished_category = Category.objects.create(
            is_published=False,
            name='test category 2',
            slug='unpublished_category',
            weight='100',
        )
        cls.published_tag = Tag.objects.create(
            is_published=True,
            name='test tag 1',
            slug='published_tag',
        )
        cls.unpublished_tag = Tag.objects.create(
            is_published=False,
            name='test tag 2',
            slug='unpublished_tag',
        )
        cls.published_item = Item(
            name='test item 1',
            category=cls.published_category,
            text='превосходно!',
            is_on_main=True,
        )
        cls.unpublished_item = Item(
            is_published=False,
            name='test item 2',
            category=cls.published_category,
            text='превосходно!',
        )

        cls.published_item.save()
        cls.unpublished_item.save()
        cls.published_item.tags.add(cls.published_tag.pk)
        cls.published_item.tags.add(cls.unpublished_tag.pk)

    def test_homepage_show_correct_context(self):
        response = self.client.get(reverse('main:home'))
        self.assertIn('items', response.context)

    def test_published_manager_selects_only_needed_fields(self):
        item = Item.objects.published().first()

        self.assertTrue(hasattr(item, 'name'))
        self.assertTrue(hasattr(item, 'text'))
        self.assertTrue(hasattr(item, 'category'))

        self.assertIsNotNone(item.category)
        self.assertTrue(hasattr(item.category, 'name'))

    def test_homepage_count_item(self):
        response = self.client.get(reverse('main:home'))
        items = response.context['items']
        self.assertEqual(items.count(), 1)

    def test_prefetched_objects_cache_exists(self):
        items = Item.objects.published()
        for item in items:
            self.assertTrue(hasattr(item, '_prefetched_objects_cache'))
            self.assertIn('tags', item._prefetched_objects_cache)

    def test_only_loaded_fields_are_present(self):
        """нужные поля загружены"""
        item = Item.objects.published().first()
        self.assertTrue(hasattr(item, 'name'))
        self.assertTrue(hasattr(item, 'text'))
        self.assertTrue(hasattr(item, 'category_id'))

    def test_deferred_fields_are_not_loaded(self):
        """поля из defer() не загружены"""
        item = Item.objects.published().first()

        self.assertNotIn('is_published', item.__dict__)
        self.assertNotIn('is_on_main', item.__dict__)
        self.assertNotIn('normalized_name', item.__dict__)

    def test_access_to_deferred_field_loads_it(self):
        """deferred поля догружаются при обращении"""
        item = Item.objects.published().first()
        self.assertNotIn('is_published', item.__dict__)
        _ = item.is_published
        self.assertIn('is_published', item.__dict__)
