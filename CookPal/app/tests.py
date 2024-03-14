from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Recipe, UserAccount, Support, Reported_Recipe

class ViewTestCase(TestCase):
    # Test the views
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='It12345')
        self.user.save()
        self.user_account = UserAccount.objects.create(
        user=self.user,
        Email='testuser@example.com',
        PhoneNumber='1234567890',
        Nickname='Test User')
        self.user_account.save()
        # Create a recipe
        self.recipe = Recipe.objects.create(
            RecipeID='testrecipe',
            Title='Test Recipe',
            Image = None,
            Ingredients='Test Ingredients',
            Instructions='Test Instructions',
            Type='Test Type',
            Origin='Test Origin',
            PostDate='2023-01-01',
            UpdateDate='2023-01-01',
            User=self.user_account
        )
        self.recipe.save()

    # Test the homepageview
    def test_homepage_view_get(self):
        response = self.client.get(reverse('app:homepage'))
        self.assertTemplateUsed(response, 'app/homepage.html')
    
    ## homepageview post function needs to be tested in real actions

    # Test the aboutview
    def test_about_view(self):
        response = self.client.get(reverse('app:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/about.html')
    
    # Test the login
    def test_login(self):
        response = self.client.post(reverse('app:login'), {'login-username': 'testuser', 'login-password': 'It12345'})
        self.assertTrue(response)
    # Test the signup
    def test_signup(self):
        response = self.client.post(reverse('app:login'), 
                                    {'username': 'testuser2', 
                                     'password': 'It12345', 
                                     'email' : 'testuser@example.com', 
                                     'phone' : '1234567890', 
                                     'nickname' : 'Test User2'})
        self.assertEqual(response.status_code, 200)
        response2 = self.client.post(reverse('app:login'), {'login-username': 'testuser2', 'login-password': 'It12345'})
        self.assertTrue(response2)
    # Test the logout
    def test_logout(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.get(reverse('app:logout'))
        self.assertFalse(response.context['user'].is_authenticated)

    # Test the reportview
    def test_report_view_get(self):
        response = self.client.get(reverse('app:report', kwargs={'reportid': self.recipe.RecipeID}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/report.html')
        
    ## reportview post function needs to be tested in real actions
    
    # Test the contactusview
    def test_contactus_view_get(self):
        response = self.client.get(reverse('app:contactus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/contactus.html')

    # Test the creatview
    def test_create_view_get(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.get(reverse('app:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/create.html')
    
    def test_creat_view_post(self):
        self.client.login(username='testuser', password='It12345')
        creat_recipe = Recipe.objects.create(
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
        response = self.client.get(reverse('app:recipe', kwargs={'recipeid': creat_recipe.RecipeID}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/recipe.html')
        self.assertContains(response, 'Test Recipe 2')

    # Test the recipeview
    def test_recipe_view_get(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.get(reverse('app:recipe', kwargs={'recipeid': self.recipe.RecipeID}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/recipe.html')
        self.assertContains(response, 'Test Recipe')
    
    ## recipeview post needs to be tested in real actions
    
    # Test the generalsupportview
    def test_generalsupport_view_get(self):
        response = self.client.get(reverse('app:generalsupport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/generalsupport.html')
    
    def test_generalsupport_view_post(self):
        response = self.client.post(reverse('app:generalsupport'), 
                                    {'email': 'user1@example.com',
                                     'title': 'Mr',
                                     'name': 'Test User',
                                     'phone': '1234567890',
                                     'problemDescription': 'I need help with my account.'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Support.objects.filter(Email='user1@example.com').exists())
        # send email needs to be tested in real actions
    
    # Test the technicalsupportview
    def test_technicalsupport_view_get(self):
        response = self.client.get(reverse('app:technicalsupport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/technicalsupport.html')
    
    def test_technicalsupport_view_post(self):
        response = self.client.post(reverse('app:technicalsupport'), 
                                    {'email': 'user2@example.com',
                                     'title': 'Mr',
                                     'name': 'Test User',
                                     'phone': '1234567890',
                                     'problemDescription': 'I need help with my account.'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Support.objects.filter(Email='user2@example.com').exists())
        # send email needs to be tested in real actions

    # Test the accountsupportview
    def test_accountsupport_view_get(self):
        response = self.client.get(reverse('app:accountsupport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/accountsupport.html')
    
    def test_accountsupport_view_post(self):
        response = self.client.post(reverse('app:accountsupport'), 
                                    {'email': 'user3@example.com',
                                     'title': 'Mr',
                                     'name': 'Test User',
                                     'phone': '1234567890',
                                     'problemDescription': 'I need help with my account.'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Support.objects.filter(Email='user3@example.com').exists())
        # send email needs to be tested in real actions

    # Test the profileview
    def test_profile_view_get(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.get(reverse('app:profile', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/profile.html')

    def test_profile_view_post(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.post(reverse('app:profile', kwargs={'username': 'testuser'}), {'button': 'myRecipes'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
    
    # Test the settingsview
    def test_settings_view_get(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.get(reverse('app:settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/settings.html')
    
    def test_settings_view_post(self):
        self.client.login(username='testuser', password='It12345')
        response = self.client.post(reverse('app:settings'), {
            'username': 'New Nickname',
            'email': 'newemail@example.com',
            'phone': '0987654321',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)

