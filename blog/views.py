from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def base(request):
    return render(request, 'blog/base.html')


def legal(request):
    return render(request, 'blog/legal.html')
