from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
    fortuneList = ['You will become very rich!',
            'You will fall into a big hole!',
            'You will find a worm in your next apple!',
            'You will lose your umbrella!',
            'You will dig up some treasure at the beach!',
            'You will turn into a newt!',
            'You will get no homework tomorrow!',
            'You will get eaten by a dragon!']
    
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune}

    return render(request, "randomfortune/fortune.html", context)