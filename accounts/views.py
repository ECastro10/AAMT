from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Member, Instrument

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        bio = request.POST['bio']
        instruments = request.POST['instruments']
        password = request.POST['password']

        user = Member()

        user.username = username
        user.email = email
        user.bio = bio
        user.instruments = instruments
        user.set_password(password)
        if request.FILES:
            user.image = request.FILES['photo']

        user.save()

        instrument_list = instruments.split(', ')
        for i in instrument_list:
            instrument = Instrument()
            instrument.name = i
            instrument.member = user
            instrument.save()


        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
        return HttpResponseRedirect('/')

    return render(request, 'register.html', {})

def dashboard(request, mbr):
    member = Member.objects.get(username=mbr)
    instruments = Instrument.objects.filter(member=member)
    context_dict = {'member': member, 'instruments': instruments}
    return render(request, 'dashboard.html', context_dict)
