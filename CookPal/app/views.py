import datetime
import json

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


#currently importing all for simplicity
from app.models import UserAccount, User, Recipe

from app.forms import RecipeForm


class HomepageView(View):
    def get(self, request):
        return render(request, 'app/homepage.html')

    def post(self, request):
        #we take this to another html?
        print(request.POST.get('search-submit'))
        print(request.POST.get('type-submit'))
        print(request.POST.get('origin-submit'))
        print(request.body)
        return render(request, 'app/homepage.html')



class AboutView(View):
    def get(self, request):
        return render(request, 'app/about.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'app/contactus.html')

class GeneralSupportView(View):
    def get(self, request):
        return render(request, 'app/generalsupport.html')

#Made changes to the View page
'''
class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html')

    def post(self, request):
        # Check if the request is for user registration
        if 'login-username' not in request.POST:
            username = request.POST.get('Signup-username')
            password = request.POST.get('Signup-password')
            nickname = request.POST.get('Signup-Nickname')
            email = request.POST.get('email')
            phoneNumber = request.POST.get('phone')

            print(username, password)
            print(nickname, email, phoneNumber)

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists. Choose a different username.")

            newUser = User.objects.create_user(username=username, password=password)
            newUserAccount = UserAccount(user=newUser, Nickname=nickname, Email=email, PhoneNumber=phoneNumber)
            newUserAccount.save()
            return render(request, 'app/homepage.html')

        else:
            username = request.POST.get('login-username')
            password = request.POST.get('login-password')
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('app:homepage'))
                else:
                    return HttpResponse("ACCOUNT DISABLED")
            else:
                print(f"Invalid login details: {username}, {password}")
                return HttpResponse("INVALID LOGIN")

            return render(request, 'app/login.html')
'''
class ReportView(View):
    def get(self, request):
        return render(request, 'app/report.html')

class TechnicalSupportView(View):
    def get(self, request):
        return render(request, 'app/technicalsupport.html')

    def post(self, request):
        print(request.body)
        return render(request, 'app/technicalsupport.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'app/homepage.html')

class AccountSupportView(View):
    def get(self, request):
        return render(request, 'app/accountsupport.html')


class CreateView(View):
    def get(self, request):
        return render(request, 'app/create.html')

    def post(self, request):
        recipe_name = request.POST.get('recipe_name')
        type = request.POST.get('type')
        origin = request.POST.get('origin')
        ingredients = request.POST.get('ingredients')
        instruction = request.POST.get('instructions')

        user = User.objects.get(username=request.user.username)

        newRecipe = Recipe(User=UserAccount.objects.get(user=request.user),
                            RecipeID = recipe_name, Title = recipe_name, Ingredients = ingredients,
                           Type = type, Origin = origin,
                           Instructions = instruction, PostDate = datetime.datetime.now(),
                           UpdateDate = datetime.datetime.now())
        newRecipe.save()
        print("saving recipe")
        #someone test why this wont work --
        return redirect(reverse('app:recipe', kwargs={'recipeid': newRecipe.RecipeID}))

class RecipeView(View):

    #method for getting recipe details based on the url
    def get_recipe_details(self, recipeid):
        try:
            recipe = Recipe.objects.get(RecipeID = recipeid)

        except Recipe.DoesNotExist:
            return None

        return recipe
    def get(self, request, recipeid):
        print("RECIPE PAGE")
        #grabbing the id from the url from which we can match recipe details via the method we created earlier
        currentRecipe = self.get_recipe_details(recipeid)

        #if no valid recipe is found then this response is given
        if currentRecipe is None:
            return HttpResponse("INVALID RECIPE")

        context = {'recipe_name': currentRecipe.Title,
                   'ingredients': currentRecipe.Ingredients,
                   'instructions': currentRecipe.Instructions}
        print(context)
        return render(request, 'app/recipe.html', context=context)

class ReportView(View):
    def get(self, request):
        return render(request, 'app/report.html')
# Create your views here.
