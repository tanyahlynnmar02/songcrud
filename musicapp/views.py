from django.shortcuts import render


def index():
    return None


def index(request):
    return render(request, 'musicapp'/index.html, '{}')


def hello(request):
    return render(request, 'hello/.html', {'name': "Tanyah Marwisa"})



# Create your views here.
