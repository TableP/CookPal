import datetime
import json

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import uniqueId

# for random id gen
import hashlib
import time
import random

# currently importing all for simplicity
from app.models import UserAccount, User, Recipe, Support, Reported_Recipe, Comment, Rating



from app import models


class HomepageView(View):
    def get(self, request):
        allRecipes = Recipe.objects.all()
        context = {"recipes": allRecipes}

        return render(request, 'app/homepage.html', context=context)

    def post(self, request):

        searchTitle = request.POST.get('search-submit')
        searchType = request.POST.get('type-submit')
        originType = request.POST.get('origin-submit')

        #allows user to not submit all parameters and still search for recipes
        if "Select a type" in searchType \
                and "Select origin" not in originType:
            searchRecipes = Recipe.objects.filter(
                Origin=originType
            )


        elif "Select a type" in searchType and "Select origin" in originType\
                :
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
            )

        elif "Select a type" in searchType\
                 and "Select origin" not in originType:
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
                Origin=originType
            )
        elif "Select origin" in originType\
                 and "Select a type" not in searchType:
            searchRecipes = Recipe.objects.filter(
                Type=searchType
            )

        elif "" in searchTitle\
                and "Select a type" not in searchType and "Select origin" not in originType:
            print("search success2")
            searchRecipes = Recipe.objects.filter(
                Type=searchType,
                Origin=originType
            )
        elif "Select origin" in originType and "Select a type" in searchType:
            searchRecipes = Recipe.objects.all()

        else:
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
                Type=searchType,
                Origin=originType
            )


        context = {"recipes": searchRecipes}
        return render(request, 'app/homepage.html', context=context)


class AboutView(View):
    def get(self, request):
        return render(request, 'app/about.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'app/contactus.html')




# Made changes to the View page
class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html')

    def post(self, request):
        # Check if the request is for user registration
        if 'login-username' not in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            nickname = request.POST.get('nickname')
            email = request.POST.get('email')
            phoneNumber = request.POST.get('phone')


            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists. Choose a different username.")

            newUser = User.objects.create_user(username=username, password=password)
            newUser.save()
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
                return HttpResponse("INVALID LOGIN")

            return render(request, 'app/login.html')


class ReportView(View):
    def get(self, request, reportid):
        print(reportid)
        return render(request, 'app/report.html')

    def post(self, request, reportid):
        reportReason = request.POST.get('problemDescription')
        reportEmail = request.POST.get('email')
        recipeid = reportid
        user_instance = request.user
        user_account = UserAccount.objects.get(user=user_instance)
        reportedRecipe = Recipe.objects.get(RecipeID = recipeid)




        newReport = Reported_Recipe(ReportID = uniqueId(reportReason + reportEmail + recipeid, Reported_Recipe),
                                    User = user_account,
                                    ReportedRecipe = reportedRecipe,
                                    ReportedRecipeDescription = reportReason,
                                    ReportedDate = datetime.datetime.now())

        newReport.save()

        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:homepage')
            })

        return render(request, 'app/report.html')



class GeneralSupportView(View):
    def get(self, request):
        return render(request, 'app/generalsupport.html')

    def post(self, request):
        email = request.POST.get('email')
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problemDescription = request.POST.get('problemDescription')


        newSupport = Support(SupportID=uniqueId(title + name + email, Support),
                                     Title=title, Name=name, Email=email, Phone=phone,
                                     SupportDescription=problemDescription,
                                     SupportDate=datetime.datetime.now())
        newSupport.save()
        if email is not None:
            send_mail(
                        'Technical Support Request Received',
                        'Thank you for your request, we will look into it as soon as possible.',
                        'cookpal27@gmail.com',
                        [email],
                        fail_silently=False,  # if have fault, don't report to the service
            )

        # use this to redirect user to maybe a thank you for submitting problem html
        if request.is_ajax():
            return JsonResponse({
                        'success': True,
                        'url': reverse('app:homepage')
            })
        return render(request, 'app/generalsupport.html')
class TechnicalSupportView(View):
    def get(self, request):
        return render(request, 'app/technicalsupport.html')

    def post(self, request):
        email = request.POST.get('email')
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problemDescription = request.POST.get('problemDescription')

        newSupport = Support(SupportID=uniqueId(title + name + email, Support),
                             Title=title, Name=name, Email=email, Phone=phone,
                             SupportDescription=problemDescription,
                             SupportDate=datetime.datetime.now())
        newSupport.save()
        if email is not None:
            send_mail(
                'Technical Support Request Received',
                'Thank you for your request, we will look into it as soon as possible.',
                'cookpal27@gmail.com',
                [email],
                fail_silently=False,  # if have fault, don't report to the service
            )

        # use this to redirect user to maybe a thank you for submitting problem html
        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:homepage')
            })
        return render(request, 'app/technicalsupport.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'app/homepage.html')


class AccountSupportView(View):
    def get(self, request):
        return render(request, 'app/accountsupport.html')

    def post(self, request):
        email = request.POST.get('email')
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problemDescription = request.POST.get('problemDescription')

        newSupport = Support(SupportID=uniqueId(title + name + email, Support),
                             Title=title, Name=name, Email=email, Phone=phone,
                             SupportDescription=problemDescription,
                             SupportDate=datetime.datetime.now())
        newSupport.save()
        if email is not None:
            send_mail(
                'Account Support Request Received',
                'Thank you for your request, we will look into it as soon as possible.',
                'cookpal27@gmail.com',
                [email],
                fail_silently=False,  # if have fault, don't report to the service
            )

        # use this to redirect user to maybe a thank you for submitting problem html
        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:homepage')
            })
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
        picture = request.FILES.get('image')
        user = User.objects.get(username=request.user.username)


        newRecipe = Recipe(User=UserAccount.objects.get(user=request.user),
                           RecipeID=recipe_name, Title=recipe_name, Ingredients=ingredients,
                           Type=type, Origin=origin,
                           Instructions=instruction, PostDate=datetime.datetime.now(),
                           UpdateDate=datetime.datetime.now())

        uniqueID = models.uniqueId(request.user.username + "-" + recipe_name, newRecipe)
        newRecipe.RecipeID = uniqueID

        if picture is not None:
            newRecipe.Image = picture
        else:
            print("no image")
        newRecipe.save()
        # due to ajax sending json we must respond with json when attempting a redirect
        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:recipe', kwargs={'recipeid': newRecipe.RecipeID})
            })

        return redirect(reverse('app:recipe', kwargs={'recipeid': newRecipe.RecipeID}))


class RecipeView(View):

    # method for getting recipe details based on the url
    def get_recipe_details(self, recipeid):
        try:
            recipe = Recipe.objects.get(RecipeID=recipeid)

        except Recipe.DoesNotExist:
            return None

        return recipe

    def get(self, request, recipeid):
        recipeuserAccounts = None;
        # grabbing the id from the url from which we can match recipe details via the method we created earlier
        currentRecipe = self.get_recipe_details(recipeid)
        try:
            recipeuserAccount = currentRecipe.User

        except UserAccount.DoesNotExist:
            testuser = User.objects.create_user(username='testuser', password='12345')
            user_account = UserAccount.objects.create(user=testuser,
                                                    Email='testuser@example.com',
                                                    PhoneNumber='1234567890',
                                                    Nickname='Test User')
            currentRecipe.User = user_account
            currentRecipe.save()


        browsingUserAccount = None
        if request.user.is_authenticated:
            browsingUser = User.objects.get(username=request.user.username)
            browsingUserAccount = UserAccount.objects.get(user=browsingUser)
        recipeOwnerNickname = recipeuserAccount.Nickname
        # if no valid recipe is found then this response is given
        if currentRecipe is None:
            return HttpResponse("INVALID RECIPE")

        context = {'recipe_name': currentRecipe.Title,
                   'ingredients': currentRecipe.Ingredients,
                   'instructions': currentRecipe.Instructions,
                   'recipeID': currentRecipe.RecipeID,
                   'username': request.user.username,
                   'recipeUserOwner': recipeOwnerNickname,
                   'recipeUsername': recipeuserAccount,
                   'userAccount': browsingUserAccount,
                   'currentRecipe': currentRecipe,
                   }
        return render(request, 'app/recipe.html', context=context)

    def post(self, request, recipeid):

        buttonType = request.POST.get('buttonType')
        currentRecipe = self.get_recipe_details(recipeid)

        #based on the button value these two can occur
        #adds to favourites
        if "1" in buttonType:
            user = User.objects.get(username=request.user.username)
            userAccount = UserAccount.objects.get(user=user)
            userFavourites = userAccount.Favourites
            userFavourites.add(currentRecipe)
            userAccount.save()
        #removes from favourites
        if "2" in buttonType:
            user = User.objects.get(username=request.user.username)
            userAccount = UserAccount.objects.get(user=user)
            userFavourites = userAccount.Favourites
            userFavourites.remove(currentRecipe)
            userAccount.save()

        if "3" in buttonType:
            return JsonResponse({
                'success': True,
                'url': reverse('app:report', kwargs={'reportid': recipeid})
            })


        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:recipe', kwargs={'recipeid': recipeid})
            })


class ProfileView(View):
    def get(self, request, username):

        allRecipes = None
        user = User.objects.get(username=username)
        userAccount = UserAccount.objects.get(user=user)
        username = userAccount.Nickname
        email = userAccount.Email
        category = request.GET.get('category')
        context = {"username": username, "email": email, "type": "Recipes"}
        if category:
            favourites = userAccount.Favourites.all()
            if favourites:
                allRecipes = favourites
                context['type'] = "Favourite Recipes"
            else:
                allRecipes = Recipe.objects.filter(User = userAccount)

        image = userAccount.Image



        if allRecipes is not None:
            context["recipes"] = allRecipes

        if image is not None:
            context["image"] = image

        return render(request, 'app/profile.html', context=context)

    def post(self, request, username):
        user = User.objects.get(username=username)
        button = request.POST.get('button').strip()
        userAccount = UserAccount.objects.get(user=user)
        username = userAccount.Nickname
        email = userAccount.Email
        recipes = Recipe.objects.all()

        context = {"username": username,
                   "email": email,
                   "recipes": recipes,
                   "type": "Recipes"}
        #handles the input button value
        if "favourite" in button:
            favourites = userAccount.Favourites.all()
            if favourites:
                recipes = favourites
                context['type'] = "Favourite Recipes"
            else:
                recipes = None

        if "myRecipes" in button:
            recipes = Recipe.objects.filter(User=userAccount)

        if "create" in button:
            return redirect(reverse('app:create'))




        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:profile', kwargs={'username': username})
            })

        return render(request, 'app/profile.html', context=context)


class SettingsView(View):
    def get(self, request):
        user = request.user
        userAccount = UserAccount.objects.get(user=user)
        image = userAccount.Image

        return render(request, 'app/settings.html', context={"image": image})

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        userAccount = UserAccount.objects.get(user=user)

        buttonFunction = request.POST.get('changeImage')


        if buttonFunction is not None:
            print("changing image")
            image = request.FILES.get('image')
            if image is not None:
                userAccount.Image = image
                userAccount.save()


        else:
            username = request.POST.get('username').strip()
            email = request.POST.get('email').strip()
            phone = request.POST.get('phone').strip()
            password = request.POST.get('password').strip()

            #checks if the fields are blank or not, if not then they will be updated with changes saved on model object
            if username is not "":
                userAccount.Nickname = username
                userAccount.save()


            if email is not "":
                userAccount.Email = email
                userAccount.save()


            if phone is not "":
                userAccount.PhoneNumber = phone
                userAccount.save()


            #this is not happening in time
            if password is not "":
                user.password = password
                print("empty password")
                user.save()

        # due to ajax sending json we must respond with json when attempting a redirect
        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:settings')
            })

        return render(request, 'app/settings.html')



