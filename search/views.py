from django.shortcuts import render
from .forms import SearchForm
from spaces.models import House , Landlord , Client
from django.db.models import Q
from django.shortcuts import Http404

# Create your views here.

def get_result(value, choice = 1):
    #the case where the user select all checkbox
    if (choice == 1):
        try:
            value = int(value)
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent=int(value))|Q(house_deposit=int(value))))
        except ValueError:
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)))
        if not houses_list:
            houses = houses_list = []
        try:
            value = int(value)
            clients_list = list(Client.objects.filter(
                Q(kind_desire__icontains=value) | Q(rooms_number_desire__icontains=int(value)) | Q(rent_proposal__icontains=int(value))| Q(deposit_proposal__icontains=int(value))))
        except ValueError:
            clients_list = list(Client.objects.filter(Q(kind_desire__icontains=value)))
        if not clients_list:
            clients = clients_list = []
        try:
            value = int(value)
           landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
            Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |
            Q(houses__house_area__icontains=value) |Q(houses__house_rent=int(value))|Q(houses__house_deposit=int(value))))
        except ValueError:
           landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
            Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |
            Q(houses__house_area__icontains=value) ))
        if not landlords_list:
             landlords = landlords_list = []

     #The case where house checkbox is selected
    elif choice == 2:
        try:
            value = int(value)
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent =int(value)) |Q(house_deposit=int(value))))
        except ValueError:
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)))
        if not houses_list:
            houses = houses_list = []

    #The case where client checkbox is selected
    elif choice == 3:
        try:
            value = int(value)
            clients_list = list(Client.objects.filter(
                Q(kind_desire__icontains=value) | Q(rooms_number_desire=int(value)) | Q(rent_proposal = int(value))|Q(deposit_proposal = int(value))|
                Q(user__username__icontains = value)|Q(user__first_name__icontains = value)|Q(user__last_name__icontains = value)))
        except ValueError:
            clients_list = list(Client.objects.filter(
                Q(kind_desire__icontains=value) |Q(user__username__icontains = value)|Q(user__first_name__icontains = value)|Q(user__last_name__icontains = value)))
                #We will look for different clients registered which are looking for a particular house or with a particular name
        if not clients_list:
            clients = clients_list = []
            
            
    #The case where landlord checkbox is selected
    elif choice == 4:
        try:
            value = int(value)
            landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
            Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |
            Q(houses__house_area__icontains=value) |Q(houses__house_rent=int(value))|Q(houses__house_deposit=int(value))))
        except ValueError:
            landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
            Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |Q(houses__house_area__icontains=value) ))
            #We will look for different landlords registered which own a particular house or with a particular name
        if not landlords_list:
            landlords = landlords_list = []
         
            
    if (len(clients_list) > 0 or len(houses_list) > 0 or len(landlords_list)> 0):
            clients = clients_list
            houses = houses_list 
            landlords = landlords_list
    context = {'clients':clients, 'clients_list':clients_list, 'houses':houses, 'houses_list':houses_list,'landlords':landlords,'landlords_list':landlords_list}
    return context


def get_result_two(value , choice1 , choice2):
    #The case where house and client checkbox are selected
    if ((choice1 == 2 and  choice1 ==3) or (choice1 == 3 and choice2 == 2)):
        try:
            houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent =int(value)) |Q(house_deposit=int(value))))
        except :
            houses = houses_list = []
        try:
            clients_list = list(Client.objects.filter(
                Q(kind_desire__icontains=value) | Q(rooms_number_desire=int(value)) | Q(rent_proposal = int(value))|Q(deposit_proposal = int(value))|
                Q(user__username__icontains = value)|Q(user__first_name__icontains = value)|Q(user__last_name__icontains = value)))
            #We will look for different clients registered which are looking for a particular house or with a particular name
        except:
            clients = clients_list = []
            
            
    #The case where house and landlord checkbox are selected
    if((choice1 == 2 and choice2 == 4) or (choice1 == 4 and choice2 == 2)):
        houses_list = list(House.objects.filter(
            Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent =int(value)) |Q(house_deposit=int(value))))
        houses = houses_list = []
        if not houses_list:
            houses = houses_list = []
        landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
        Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |
         Q(houses__house_area__icontains=value) |Q(houses__house_rent=int(value))|Q(houses__house_deposit=int(value))))
         #We will look for different landlords registered which own a particular house or with a particular name
        if not landlords_list:
            landlords = landlords_list = []
    #The case where client and landlord checkbox are selected
    if((choice1 == 3 and choice2 == 4) or (choice1 == 4 and choice2 == 3)):
        clients_list = list(Client.objects.filter(
            Q(kind_desire__icontains=value) | Q(rooms_number_desire=int(value)) | Q(rent_proposal = int(value))|Q(deposit_proposal = int(value))|
            Q(user__username__icontains = value)|Q(user__first_name__icontains = value)|Q(user__last_name__icontains = value)))
            #We will look for different clients registered which are looking for a particular house or with a particular name
        if not clients_list:
            clients = clients_list = []
    #The case where landlord checkbox is selected
        landlords_list = list(Landlord.objects.filter(Q(user__username__icontains = value)| Q(user__first_name__icontains=value)| 
            Q(user__last_name__icontains=value)| Q(houses__house_township__icontains=value) |
            Q(houses__house_area__icontains=value) |Q(houses__house_rent=int(value))|Q(houses__house_deposit=int(value))))
            #We will look for different landlords registered which own a particular house or with a particular name
        if not landlords_list:
            landlords = landlords_list = []
    context = {'clients':clients, 'clients_list':clients_list, 'houses':houses, 'houses_list':houses_list,'landlords':landlords,'landlords_list':landlords_list}
    return context
        
def search(request , query):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            value = form.cleaned_data['query']
            value_for_all = form.cleaned_data['query_for_all']
            value_for_house = form.cleaned_data['query_for_house']
            value_for_client = form.cleaned_data['query_for_client']
            value_for_landlord = form.cleaned_data['query_for_landlord']
            values_array = [value_for_all,value_for_house , value_for_client, value_for_landlord]
            if values_array[0]:
                context = get_result(value)
            elif values_array[1]:
                context = get_result(value, 2)
            elif values_array[2]:
                context = get_result(value, 3)
            elif values_array[3]:
                context = get_result(value, 4)
            elif (values_array[1] and values_array[2]):
                context = get_result_two(value, 2, 3)
            elif (values_array[1] and values_array[3]):
                context = get_result_two (value, 2, 4)
            elif (values_array[2] and values_array[3]):
                context = get_result_two (value, 3, 4)
            else:
                context = get_result(value)
    return render(request, 'search/search_house.html', locals())

def test(value):
    try:
        value = int(value)
        houses_list = list(House.objects.filter(
        Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)|Q(house_rent=int(value))|Q(house_deposit=int(value))))
    except ValueError:
        houses_list = list(House.objects.filter(
        Q(house_township__icontains=value) | Q(house_area__icontains=value) |Q(house_kind__icontains=value)))
    if not houses_list:
        houses = houses_list = []
    return houses_list
