from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)


def about(request):

    context_dict = {}
    return render(request, 'about.html', context_dict)


def contact(request):

    context_dict = {}
    return render(request, 'contact.html', context_dict)


def theory(request):

    context_dict = {}
    return render(request, 'theory.html', context_dict)


def log_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/' + str(user.username))
    return render(request, 'login.html', {})


def logout_view(request):

    logout(request)
    return HttpResponseRedirect('/')
