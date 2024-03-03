# Generated by Django 2.1.5 on 2024-03-03 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('CollectionID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('CollectionName', models.CharField(max_length=255)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('CommentID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=200)),
                ('CommentDate', models.DateTimeField()),
                ('ParentCommentID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcomment', to='app.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('RatingID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('RatingNumber', models.IntegerField(verbose_name=5)),
                ('Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('RecipeID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Ingredients', models.CharField(max_length=200)),
                ('Instructions', models.CharField(max_length=500)),
                ('PostDate', models.DateTimeField()),
                ('UpdateDate', models.DateTimeField()),
                ('Collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='app.Collection')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reported_Recipe',
            fields=[
                ('ReportID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('ReportedRecipeDescription', models.CharField(max_length=200)),
                ('ReportedDate', models.DateTimeField()),
                ('ReportedRecipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Recipe')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Site_Admin',
            fields=[
                ('AdminID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('AdminName', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('PhoneNumber', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('UserID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('PhoneNumber', models.CharField(max_length=30)),
                ('Nickname', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Support',
            fields=[
                ('Admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.Site_Admin')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='Recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='rating',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='comment',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reported_recipe',
            name='Customer_Support',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_recipes', to='app.Customer_Support'),
        ),
    ]
