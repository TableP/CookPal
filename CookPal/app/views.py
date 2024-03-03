
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View
from django.http import HttpResponse


#currently importing all for simplicity
from app.models import UserAccount, User


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

class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html')


    def post(self, request):
        #checks if button pressed is login or register
        #if registering then this block is ran
        if request.POST.get('login-username') is None:
            username = request.POST.get('Signup-username')
            password = request.POST.get('Signup-password')
            nickname = request.POST.get('Signup-Nickname')
            email = request.POST.get('email')
            phoneNumber = request.POST.get('phone')

            print(username, password)
            print(nickname, email, phoneNumber)

            newUser = User.objects.create_user(username=username, password=password)
            newUserAccount = UserAccount(user=newUser,Nickname=nickname, Email=email, PhoneNumber=phoneNumber)
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
# Create your views here.
