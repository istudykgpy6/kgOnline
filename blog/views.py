from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")

def gogogo(request):
    return render(request, "blog/gogogo.html")

