from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, Http404
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from userManagmentApp.forms import MyRegistrationForm, UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.template import loader
from django.template.context_processors import csrf
from django.http import Http404, JsonResponse
from django.core.mail import send_mail

def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': MyRegistrationForm()}
    # send_mail('You were successfully registered on SMART GOAL portal', 'Thank you for joining us!
    # Lets be more effective!',
    # 'chernyshova.anastasia@gmail.com', [user.email], fail_silently=False)
    return render(request, 'registration.html', context)
