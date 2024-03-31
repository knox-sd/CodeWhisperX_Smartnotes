from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView #vlass base view
from django.contrib.auth.mixins import LoginRequiredMixin #for authozation login
from django.contrib.auth.views import LoginView, LogoutView

##Class Base Views

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthoriizdView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/sujan'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'



### normal views set ##
# def home(request):
#     # return HttpResponse('Hello, World')
#     return render(request, 'home/welcome.html',{'today': datetime.today()})


# @login_required(login_url='/admin') #route the authorized page to Admin login
# def authorized(request):
#     return render(request, 'home/authorized.html', {})