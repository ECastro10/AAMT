from django.shortcuts import render

# Create your views here.
def tuner(request):
    context_dict = {}
    return render(request, 'tuner.html', context_dict)


def tuner2(request):
    context_dict = {}
    return render(request, 'tuner2.html', context_dict)