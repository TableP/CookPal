
from django.contrib import admin
from django.urls import path
from django.urls import include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact-us/', views.ContactUsView.as_view(), name='contactus'),
##    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('report/<reportid>/', views.ReportView.as_view(), name='report'),

    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('settings/', views.SettingsView.as_view(), name='settings'),

    path('general-support/', views.GeneralSupportView.as_view(), name='generalsupport'),
    path('technical-support/', views.TechnicalSupportView.as_view(), name='technicalsupport'),
    path('account-support/', views.AccountSupportView.as_view(), name='accountsupport'),


    path('create/', views.CreateView.as_view(), name='create'),
    path('recipe/<recipeid>/', views.RecipeView.as_view(), name='recipe'),

]
