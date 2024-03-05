
from django.contrib import admin
from django.urls import path
from django.urls import include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact-us/', views.ContactUsView.as_view(), name='contactus'),
    path('general-support/', views.GeneralSupportView.as_view(), name='generalsupport'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('technical-support/', views.TechnicalSupportView.as_view(), name='technicalsupport'),
]