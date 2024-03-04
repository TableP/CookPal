from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, Site_Admin, Collection, Recipe, Comment, Rating, Reported_Recipe

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['Email', 'PhoneNumber', 'Nickname']

class SiteAdminForm(forms.ModelForm):
    class Meta:
        model = Site_Admin
        fields = ['AdminID', 'AdminName', 'Password', 'Email', 'PhoneNumber']

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['CollectionID', 'User', 'CollectionName']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['RecipeID', 'User', 'Collection', 'Title', 'Ingredients', 'Instructions', 'PostDate', 'UpdateDate']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['CommentID', 'User', 'Recipe', 'ParentCommentID', 'Comment', 'CommentDate']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['RatingID', 'User', 'Comment', 'Recipe', 'RatingNumber']

class ReportedRecipeForm(forms.ModelForm):
    class Meta:
        model = Reported_Recipe
        fields = ['ReportID', 'User', 'Customer_Support', 'ReportedRecipe', 'ReportedRecipeDescription', 'ReportedDate']
