from django.shortcuts import render
from time import localtime, strftime
# Create your views here.


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request, 'index.html', context)
