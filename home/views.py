from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin #for authozation login

##Class Base Views

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthoriizdView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/sujan'


### normal views set ##
# def home(request):
#     # return HttpResponse('Hello, World')
#     return render(request, 'home/welcome.html',{'today': datetime.today()})


# @login_required(login_url='/admin') #route the authorized page to Admin login
# def authorized(request):
#     return render(request, 'home/authorized.html', {})