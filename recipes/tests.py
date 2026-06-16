from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify

from recipes.models import RecipeModels


class RecipeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='ricardo',
            password='123456'
        )

    def test_recipe_str(self):
        recipe = RecipeModels(
            title='Pizza',
            description='Teste',
            author=self.user
        )

        self.assertEqual(
            str(recipe),
            'Pizza'
        )

    def test_slug_generation(self):
        recipe = RecipeModels(
            title='Pizza de Calabresa',
            description='Teste',
            author=self.user
        )

        recipe.save()

        self.assertEqual(
            recipe.slug,
            slugify(recipe.title)
        )

    def test_recipe_default_is_not_published(self):
        recipe = RecipeModels.objects.create(
            title='Lasanha',
            description='Teste',
            author=self.user
        )

        self.assertFalse(
            recipe.is_published
        )


class DashboardTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='ricardo',
            password='123456'
        )

    def test_dashboard_requires_login(self):

        response = self.client.get(
            '/dashboard/'
        )

        self.assertEqual(
            response.status_code,
            302
        )

    def test_dashboard_logged_user(self):

        self.client.login(
            username='ricardo',
            password='123456'
        )

        response = self.client.get(
            '/dashboard/'
        )

        self.assertEqual(
            response.status_code,
            200
        )


class RegisterTest(TestCase):

    def test_register_page_loads(self):

        response = self.client.get(
            '/register/'
        )

        self.assertEqual(
            response.status_code,
            200
        )


class JwtTokenTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='ricardo',
            password='123456'
        )

    def test_get_jwt_token(self):

        response = self.client.post(
            '/api/token/',
            {
                'username': 'ricardo',
                'password': '123456'
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIn(
            'access',
            response.json()
        )

        self.assertIn(
            'refresh',
            response.json()
        )
