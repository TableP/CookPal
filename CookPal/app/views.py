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
from app.models import UserAccount, User, Recipe, Support, Reported_Recipe, Comment, Rating, Favourites



from app import models


class HomepageView(View):
    def get(self, request):
        allRecipes = Recipe.objects.all()
        context = {"recipes": allRecipes}

        return render(request, 'app/homepage.html', context=context)

    def post(self, request):
        # we take this to another html?
        print(request.POST.get('search-submit'))
        print(request.POST.get('type-submit'))
        print(request.POST.get('origin-submit'))
        print(request.body)

        searchTitle = request.POST.get('search-submit')
        searchType = request.POST.get('type-submit')
        originType = request.POST.get('origin-submit')

        #allows user to not submit all parameters and still search for recipes
        if "Select a type" in searchType \
                and "Select origin" not in originType:
            print("search success5")
            searchRecipes = Recipe.objects.filter(
                Origin=originType
            )


        elif "Select a type" in searchType and "Select origin" in originType\
                :
            print("search success4")
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
            )

        elif "Select a type" in searchType\
                 and "Select origin" not in originType:
            print("search success3")
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
                Origin=originType
            )
        elif "Select origin" in originType\
                 and "Select a type" not in searchType:
            print("search success2")
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
                Type=searchType
            )

        elif "" in searchTitle\
                and "Select a type" not in searchType and "Select origin" not in originType:
            print("search success1")
            searchRecipes = Recipe.objects.filter(
                Type=searchType,
                Origin=originType
            )
        elif "Select origin" in originType and "Select a type" in searchType:
            print("search success")
            searchRecipes = Recipe.objects.all()

        else:
            print("search success-1")
            print(searchTitle)
            print(searchType)
            print(originType)
            searchRecipes = Recipe.objects.filter(
                Title=searchTitle,
                Type=searchType,
                Origin=originType
            )

        print(searchRecipes)

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


class ReportView(View):
    def get(self, request, reportid):
        return render(request, 'app/report.html')

    def post(self, request, reportid):
        reportReason = request.POST.get('reportReason')
        reportEmail = reportReason.POST.get('reportEmail')
        recipeid = reportReason.POST.get('recipeid')
        reportId = uniqueId(reportReason + reportEmail)
        reportedRecipe = Recipe.objects.get(RecipeID = recipeid)
        user = User.objects.get(username=request.user.username)

        newReport = Reported_Recipe(ReportID = reportId,
                                    User = user,
                                    Reported_Recipe = reportedRecipe,
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
        print("Working")
        email = request.POST.get('email')
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problemDescription = request.POST.get('problemDescription')

        print(email + title + name + phone + problemDescription)

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
        print("Working")
        email = request.POST.get('email')
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problemDescription = request.POST.get('problemDescription')

        print(email + title + name + phone + problemDescription)

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
        print("Working")
        email = request.POST.get('email')
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problemDescription = request.POST.get('problemDescription')

        print(email + title + name + phone + problemDescription)

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
        print("test")
        recipe_name = request.POST.get('recipe_name')
        type = request.POST.get('type')
        origin = request.POST.get('origin')
        ingredients = request.POST.get('ingredients')
        instruction = request.POST.get('instructions')
        picture = request.POST.get('image')
        user = User.objects.get(username=request.user.username)

        newRecipe = Recipe(User=UserAccount.objects.get(user=request.user),
                           RecipeID=recipe_name, Title=recipe_name, Ingredients=ingredients,
                           Type=type, Origin=origin,
                           Instructions=instruction, PostDate=datetime.datetime.now(),
                           UpdateDate=datetime.datetime.now())

        uniqueID = models.uniqueId(request.user.username + "-" + recipe_name, newRecipe)
        print(uniqueID)
        newRecipe.RecipeID = uniqueID
        if picture is not None:
            newRecipe(Image=picture)


        newRecipe.save()
        print("saving recipe")
        print(newRecipe.RecipeID)
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
        print("RECIPE PAGE")
        # grabbing the id from the url from which we can match recipe details via the method we created earlier
        currentRecipe = self.get_recipe_details(recipeid)
        try:
            recipeuser = currentRecipe.User
        except recipeuser .DoesNotExist:
            testuser = User.objects.create_user(username='testuser', password='12345')
            user_account = UserAccount.objects.create(user=testuser,
                                                    Email='testuser@example.com',
                                                    PhoneNumber='1234567890',
                                                    Nickname='Test User')
            currentRecipe.User = user_account
            currentRecipe.save()

        # user = User.objects.get(username=request.user.username)

        # if no valid recipe is found then this response is given
        if currentRecipe is None:
            return HttpResponse("INVALID RECIPE")

        context = {'recipe_name': currentRecipe.Title,
                   'ingredients': currentRecipe.Ingredients,
                   'instructions': currentRecipe.Instructions,
                   'recipeID': currentRecipe.RecipeID,
                   'username': request.user.username}
        print(context)
        return render(request, 'app/recipe.html', context=context)

    def post(self, request, recipeID):
        #logic for comments and ratings - needs testing
        recipeComment = request.POST.get('recipeComment')
        recipeRating = request.POST.get('recipeRating')
        parentCommentID = request.POST.get('parentCommentID')
        commentDate = datetime.datetime.now()
        recipe = Recipe.objects.get(RecipeID = recipeID)
        ratingNumber = request.POST.get('recipeRating')
        user = User.objects.get(username=request.user.username)

        newComment = Comment(CommentID = uniqueId(recipe + recipeComment + commentDate),
                             User = user,
                             Recipe = recipe,
                             Comment = recipeComment,
                             CommendDate = commentDate)

        if parentCommentID is not None:
            newComment(ParentCommendID = parentCommentID)

        newComment.save()

        newRating = Rating(RatingID = uniqueId(recipe + recipeComment + recipeRating + commentDate),
                           User = user,
                           Comment = newComment,
                           Recipe = recipe,
                           RatingNumber = ratingNumber)
        newRating.save()


class ProfileView(View):
    def get(self, request, username):
        print(username)

        user = User.objects.get(username=username)
        userAccount = UserAccount.objects.get(user=user)
        print(userAccount.Nickname)
        username = userAccount.Nickname
        email = userAccount.Email
        allRecipes = Recipe.objects.all()

        context = {"username": username,
                   "email": email,
                   "recipes": allRecipes}

        return render(request, 'app/profile.html', context=context)

    def post(self, request, username):
        user = User.objects.get(username=username)
        button = request.POST.get('button').strip()
        userAccount = UserAccount.objects.get(Nickname=user)
        username = userAccount.Nickname
        email = userAccount.Email
        recipes = Recipe.objects.all()
        print(button)

        if "favourite" in button:
            print("performing favourites")
            try:
                favourites = Favourites.objects.get(User=userAccount)
                favRecipes = Favourites.Recipes.all()
                recipes = favRecipes
            except Favourites.DoesNotExist:
                recipes = None


        if "myRecipes" in button:
            recipes = Recipe.objects.all()

        if "create" in button:
            return redirect(reverse('app:create'))


        context = {"username": username,
                   "email": email,
                   "recipes": recipes}

        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:profile', kwargs={'username': username})
            })

        return render(request, 'app/profile.html', context=context)


class SettingsView(View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        userAccount = UserAccount.objects.get(user=user)
        print("old nickname: " + userAccount.Nickname)
        return render(request, 'app/settings.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = User.objects.get(username=request.user.username)
        userAccount = UserAccount.objects.get(user=user)

        print(request.POST)

        print(username.strip())
        print(email)
        print(phone)
        print(password)

        if username is not None:
            userAccount.Nickname = username
            userAccount.save()
            print("empty username")
            print("new nickname: " + userAccount.Nickname)


        if email is not None:
            userAccount.Email = email
            print("empty email")

        if phone is not None:
            userAccount.PhoneNumber = phone
            print("empty phone")

        if password is not None:
            user.password = password
            print("empty password")
            user.save()

        print("new nickname: " + userAccount.Nickname)
        # due to ajax sending json we must respond with json when attempting a redirect
        if request.is_ajax():
            return JsonResponse({
                'success': True,
                'url': reverse('app:settings')
            })

        return render(request, 'app/settings.html')


# Create your views here.
