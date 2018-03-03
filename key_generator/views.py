from django.shortcuts import render

# Create your views here.

def circle_of_fifths_selector(request):
    context_dict = {}
    return render(request, 'spinning_wheel.html', context_dict)