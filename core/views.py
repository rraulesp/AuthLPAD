from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import authenticate, login, logout

import traceback
#from core.models import UserLog

# class LoginView(LoginView):
#     template_name="login.html"
    

from django.views.generic import View
from .forms import LoginForm


class LoginPageView(View):
    template_name = 'login.html'
    form_class = LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
       
        if form.is_valid():
            
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                request.session['password'] = form.cleaned_data['password']
                return redirect('home')
        message = 'Verifique las credenciales. ¡Son incorrectas!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LogoutView(LogoutView):
    pass