from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'dcsc_website/index.html', context)