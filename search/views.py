from django.shortcuts import render
from .forms import SearchForm
from spaces.models import House , Landlord , Client
from django.db.models import Q
from django.shortcuts import Http404

# Create your views here.

def get_result(value, choice = 0):
    #the case where the user select all checkbox
    if (choice == 0):
        try:
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent=int(value))|Q(house_deposit=int(value))))
        except Http404:
            houses = houses_list = []
        clients_list = list(Client.objects.filter(
            Q(kind_desire__icontains=value) | Q(rooms_number_desire__icontains=int(value)) | Q(rent_proposal__icontains=int(value))| Q(deposit_proposal__icontains=int(value))))
        landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| Q(user__last_name__icontains=value))) 
        if not clients_list:
            clients = clients_list = []
        if not landlords_list:
            landlords = landlords_list = []
        if (len(clients_list) > 0 or len(houses_list) > 0 or len(landlords_list)> 0):
            clients = clients_list
            houses = houses_list 
            landlords = landlords_list
    #The case where house checkbox is selected
    elif choice == 1:
        try:
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent =int(value)) |Q(house_deposit=int(value))))
        except Http404:
            houses = houses_list = []
        landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| Q(user__last_name__icontains=value))) 
        if not landlords_list:
            landlords = landlords_list = []
        if (len(houses_list) > 0 or len(landlords_list)> 0):
            houses = houses_list 
            landlords = landlords_list
    #The case where house checkbox is selected
    elif choice == 2:
        clients_list = list(Client.objects.filter(
            Q(kind_desire__icontains=value) | Q(rooms_number_desire=int(value)) | Q(rent_proposal = int(value))|Q(deposit_proposal = int(value))|
            Q(user__username__icontains = value)|Q(user__first_name__icontains = value)|Q(user__last_name__icontains = value)))
        if not clients_list:
            clients = clients_list = []
        if (len(houses_list) > 0):
            clients = clients_list
    elif choice == 3:
        landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
        Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |
         Q(houses__house_area__icontains=value) |Q(houses__house_rent=int(value))|Q(houses__house_deposit=int(value)))) 
        if not landlords_list:
            landlords = landlords_list = []



    context = {'channels_list':channels_list, 'channels':channels, 'houses':houses, 'houses_list':houses_list}
    return context



def search_client(request , query):
    context = {}
    return render(request, 'search/search_client.html', context)


def search_house(request , query):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            value = form.cleaned_data['query']
            value_for_all = form.cleaned_data['query_for_all']
            value_for_house = form.cleaned_data['query_for_house']
            value_for_client = form.cleaned_data['query_for_client']
            value_for_landlord = form.cleaned_data['query_for_landlord']
            values_array = [value_for_all, value_for_client, value_for_landlord]
            if values_array[0]:
                context = get_result(value)
            elif (values_array[1] and values_array[2]):
                context = get_result_two(value, 1, 2)
            elif (values_array[1] and values_array[3]):
                context = get_result_two (value, 1, 3)
            elif (values_array[2] and values_array[3]):
                context = get_result_two (value, 2, 3)
            elif values_array[1]:
                context = get_result(value, 1)
            elif values_array[2]:
                context = get_result(value, 2)
            elif values_array[3]:
                context = get_result(value, 3)
            else:
                context = get_result(value)
    return render(request, 'search/search_house.html', locals())
