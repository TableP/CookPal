import datetime

from django.db import models
from django.contrib.auth.models import User
import hashlib
import time
import random

class UserAccount(models.Model):
    #testing base authentication until real user authentication is implemented
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    Email = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=30)
    Favourites = models.ManyToManyField('Recipe', blank=True)
    Image = models.ImageField(upload_to='profile_images/', blank=True)
    #Added this by Nduka
    def __str__(self):
        return self.user.username


class Site_Admin(models.Model):
    # AdminID is the primary key
    AdminID = models.CharField(max_length=30, primary_key=True)
    # Other fields
    AdminName = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=30)
    # Get the primary key
    def __str__(self):
        return self.AdminID
    

class Customer_Support(models.Model):
    # Admin is the primary key
    # Admin and Site_Admin are one-to-one
    Admin = models.OneToOneField(Site_Admin, on_delete=models.CASCADE, primary_key=True)



class Recipe(models.Model):
    # RecipeID is the primary key
    RecipeID = models.CharField(max_length=30, primary_key=True)
    # User and Recipe are many-to-many
    User = models.ForeignKey(UserAccount,related_name="recipes", on_delete=models.CASCADE)
    # Other fields
    Image = models.ImageField(upload_to='recipe_images/', blank=True)
    Title = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Origin = models.CharField(max_length=50)
    Ingredients = models.CharField(max_length=200)
    Instructions = models.CharField(max_length=500)
    PostDate = models.DateTimeField()
    UpdateDate = models.DateTimeField()
    # Get the primary key
    def __str__(self):
        return self.RecipeID


class Comment(models.Model):
    # CommentID is the primary key
    CommentID = models.CharField(max_length=30, primary_key=True)
    # User and Comment are many-to-many
    User = models.ForeignKey(UserAccount,related_name="comments", on_delete=models.CASCADE)
    # Recipe and Comment are one-to-many
    Recipe = models.ForeignKey(Recipe,related_name="comments", on_delete=models.CASCADE)
    # ParentCommentID and Comment are one-to-many
    # Allow comment dose not have a parent comment
    ParentCommentID = models.ForeignKey('self',related_name="subcomment", on_delete=models.CASCADE, null=True, blank=True)
    # Other fields
    Comment = models.CharField(max_length=200)
    CommentDate = models.DateTimeField()
    # Get the primary key
    def __str__(self):
        return self.CommentID

class Rating(models.Model):
    # RatingID is the primary key
    RatingID = models.CharField(max_length=30, primary_key=True)
    # User and Rating are one-to-many
    User = models.ForeignKey(UserAccount,related_name="ratings", on_delete=models.CASCADE)
    # Comment and Rating are one-to-many
    Comment = models.ForeignKey(Comment, related_name="ratings", on_delete=models.CASCADE)
    # Recipe and Rating are one-to-many
    Recipe = models.ForeignKey(Recipe,related_name="ratings", on_delete=models.CASCADE)
    # Other fields
    RatingNumber = models.IntegerField(5)
    # Get the primary key
    def __str__(self):
        return self.RatingID

class Reported_Recipe(models.Model):
    # ReportID is the primary key
    ReportID = models.CharField(max_length=30, primary_key=True)
    # User and Reported_Recipe are one-to-many
    User = models.ForeignKey(UserAccount,related_name="reports", on_delete=models.CASCADE)
    # Customer_Support and Reported_Recipe are one-to-many
    #added null=true to the parameters to allow for on_delete to be able to set model to null
    Customer_Support = models.ForeignKey(Customer_Support,related_name="reported_recipes", on_delete=models.SET_NULL, null=True)
    # Recipe and Reported_Recipe are one-to-many
    ReportedRecipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    # Other fields
    ReportedRecipeDescription = models.CharField(max_length=200)
    ReportedDate = models.DateTimeField()
    # Get the primary key
    def __str__(self):
        return self.ReportID
    
class Support(models.Model):
    # SupportID is the primary key
    SupportID = models.CharField(max_length=30, primary_key=True)
    Title = models.CharField(max_length=10)
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone = models.CharField(max_length=30)
    SupportDescription = models.CharField(max_length=200)
    SupportDate = models.DateTimeField()
    # Get the primary key
    def __str__(self):
        return self.SupportID

def uniqueId(String, Model):
    # The String can be the basic information of object you get now, ex: username, email, etc.
    # String = UserAccount.email + UserAccount.Nickname + Recipe.Title 
    # String = UserAccount.email + UserAccount.Nickname + Collection.CollectionName
    # String = UserAccount.email + UserAccount.Nickname + Comment.Comment
    # String = UserAccount.email + UserAccount.Nickname + str(Rating.RatingNumber)
    #...

    # The 1-20 is the hash of string
    id20 = hashlib.md5(String.encode()).hexdigest()[:20]
    time = str(datetime.time())
    # The 21-28 is the hash of current time
    id8 = hashlib.md5(time.encode()).hexdigest()[-8:]
    # The 29-30 is the random character
    id2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=2))
    # Combine the 3 parts to get the unique id
    id = id20 + id8 + id2
    PrimaryKey = Model._meta.pk.name
    #if Model.objects.filter(**{PrimaryKey : id}).exists():
        #return uniqueId(String, Model)

    #checks if a recipe with that id already exists
    try:
        recipe = Recipe.objects.get(RecipeID=id)
        return uniqueId(String, Model)
    except Recipe.DoesNotExist:
        return id


