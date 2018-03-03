from django.shortcuts import render

# Create your views here.

def tone_generator(request):
    context_dict = {}
    return render(request, 'tone_generator.html', context_dict)
