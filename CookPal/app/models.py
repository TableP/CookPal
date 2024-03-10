from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    #testing base authentication until real user authentication is implemented
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    Email = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=30)

    #Added this by Nduka
    def __str__(self):
        return self.user.username
    # Get the primary key


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

class Collection(models.Model):
    # CollectionID is the primary key
    CollectionID = models.CharField(max_length=30, primary_key=True)
    # User and Collection are one-to-many
    User = models.ForeignKey(UserAccount,related_name="collections", on_delete=models.CASCADE)
    # Other fields
    CollectionName = models.CharField(max_length=255)
    # Get the primary key
    def __str__(self):
        return self.CollectionID
class Recipe(models.Model):
    # RecipeID is the primary key
    RecipeID = models.CharField(max_length=30, primary_key=True)
    # User and Recipe are many-to-many
    User = models.ForeignKey(UserAccount,related_name="recipes", on_delete=models.CASCADE)
    # Collection and Recipe are one-to-many
    # Allow recipe is not in any collection
    Collection = models.ForeignKey(Collection, related_name="recipes", on_delete=models.SET_NULL, null=True, blank=True)
    # Other fields
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
