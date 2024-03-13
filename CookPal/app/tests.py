from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Recipe, UserAccount

class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user_account = UserAccount.objects.create(
        user=self.user,
        Email='testuser@example.com',
        PhoneNumber='1234567890',
        Nickname='Test User')


        self.recipe = Recipe.objects.create(
            RecipeID='testrecipe',
            Title='Test Recipe',
            Ingredients='Test Ingredients',
            Instructions='Test Instructions',
            Type='Test Type',
            Origin='Test Origin',
            PostDate='2023-01-01',
            UpdateDate='2023-01-01',
            User_id=self.user.id
        )

    def test_homepage_view(self):
        response = self.client.get(reverse('app:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/homepage.html')

    def test_about_view(self):
        response = self.client.get(reverse('app:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/about.html')

    def test_login_view(self):
        response = self.client.post(reverse('app:login'), {'login-username': 'testuser', 'login-password': '12345'})
        self.assertRedirects(response, reverse('app:homepage'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('app:logout'))
        self.assertRedirects(response, reverse('app:homepage'))
        self.assertFalse(response.context['user'].is_authenticated)

    def test_report_view_get(self):
        response = self.client.get(reverse('app:report', kwargs={'reportid': self.recipe.RecipeID}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/report.html')
    
    def test_contact_us_view(self):
        response = self.client.get(reverse('app:contactus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/contactus.html')


    def test_create_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('app:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/create.html')
    
    def test_recipe_view_post(self):
        self.client.login(username='testuser', password='12345')
        test_recipe = Recipe.objects.create(
            RecipeID='recipe123',
            Title='Test Recipe 2',
            Ingredients='Test Ingredients 2',
            Instructions='Test Instructions 2',
            Type='Test Type',
            Origin='Test Origin',
            PostDate='2023-01-02',
            UpdateDate='2023-01-02',
            User=self.user_account
        )
        response = self.client.get(reverse('app:recipe', kwargs={'recipeid': test_recipe.RecipeID}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/recipe.html')
        self.assertContains(response, 'Test Recipe 2')

    def test_profile_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('app:profile', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/profile.html')


