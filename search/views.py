from django.shortcuts import render

# Create your views here.


def search_client(request):
    context = {}
    return render(request, 'search/search_client.html', context)


def search_house(request):
    context = {}
    return render(request, 'search/search_house.html', context)
