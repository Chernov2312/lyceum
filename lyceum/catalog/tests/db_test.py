from django.core.exceptions import ValidationError
import django.test
from django.test import override_settings
from parameterized import parameterized

from catalog.models import Category, Item, Tag

__all__ = [
    'CategoryModelTest',
    'ItemModelTest',
    'LengthTest',
    'TagModelTest',
    'UniqueNameTest',
]


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
            ('гений123', 'гений'),
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
