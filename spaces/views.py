from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import SignUpForm, SignInForm, EditForm, AddHouseForm
from django.contrib.auth.models import User
from .models import Client, Landlord, House
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from spaces.models import Client, Landlord
import re
import os
from PIL import Image 
from search.forms import SearchForm

houses_path= os.path.abspath("C:/Users/XC-DEV-3/Documents/projet soutenance/logeique2/media/img/houses")
avatars_path = os.path.abspath("C:/Users/XC-DEV-3/Documents/projet soutenance/logeique2/media/img/avatars")

max_height= 540
max_width= 304
extensions= ['PNG','JPG']

def adjusted_size(width,height):
    if width>max_width or height>max_height:
        if width>height:
            return max_width, int (max_width * height/ width)
        else:
            return int (max_height*width/height), max_height
    else:
        return width,height

  
def resize(path , f): 
    try:
        if f in os.listdir(path):
            if os.path.isfile(os.path.join(path,f)):
                f_text, f_ext= os.path.splitext(f)
                f_ext= f_ext[1:].upper()
                if f_ext in extensions:
                    image = Image.open(os.path.join(path,f))
                    width, height= image.size
                    image = image.resize(adjusted_size(width , height))
                    return f
    except IOError: 
        pass

def is_valid_contact(number):
    contact_valid = False
    phoneRegex = re.compile(r'''(
        (\+?\d{1,3}|\+?\(\d{1,3}\))?#Area code
        (\s|-)? #separator 
        \d{2} #Deux premiers chiffres
        (-) #separator
        \d{2} #Deux deuxiemes
        (-) #separator
        \d{2}
        (-) #separator
        \d{2}
        )''', re.VERBOSE
                            )

    mo = phoneRegex.search(number)
    if mo == None:
        contact_valid = False
    else:
        contact_valid = True
    return contact_valid

# Create your views here.


def home(request):
    form = SearchForm()
    return render(request, 'spaces/index.html', locals())


def sign_up(request):
    form = SignUpForm()
    users = User.objects.all()
    clients = Client.objects.all()
    landlords = Landlord.objects.all()
    email_unique_error = False
    pass_different_err = False
    contact_exist_error = False
    invalid_contact_err = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            client = form.cleaned_data['client']
            landlord = form.cleaned_data['landlord']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['password_verification']

            if is_valid_contact(contact) == False:
                invalid_contact_err = True
                return render(request, 'spaces/signup.html', locals())

            if password1 == password2:
                if client:
                    if email:
                        for each_user in users:
                            each_user.email = each_user.email.lower()
                            email = email.lower()
                            if each_user.email == email:
                                email_unique_error = True
                                return render(request, 'spaces/signup.html', locals())

                        for each_client in clients:
                            each_client.contact = each_client.contact.split(
                                '-')
                            each_client.contact = "".join(each_client.contact)
                            contact_mo = contact.split('-')
                            contact_mo = "".join(contact)
                            if each_client.contact == contact_mo:
                                contact_exist_error = True
                                return render(request, 'spaces/signup.html', locals())
                        user = User.objects.create_user(
                            username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                        user.save()
                        client = Client(user=user, contact=contact)
                        client.save()

                    elif not email:
                        for each_client in clients:
                            each_client.contact = each_client.contact.split(
                                '-')
                            each_client.contact = "".join(each_client.contact)
                            contact_mo = contact.split('-')
                            contact_mo = "".join(contact)
                            if each_client.contact == contact_mo:
                                contact_exist_error = True
                                return render(request, 'spaces/signup.html', locals())
                        user = User.objects.create_user(
                            username=username, first_name=first_name, last_name=last_name, password=password1)
                        user.save()
                        client = Client(user=user, contact=contact)
                        client.save()

                elif landlord:
                    if email:
                        for each_user in users:
                            each_user.email = each_user.email.lower()
                            email = email.lower()
                            if each_user.email == email:
                                email_unique_error = True
                                return render(request, 'spaces/signup.html', locals())
                        for each_landlord in landlords:
                            each_landlord.contact = each_landlord.contact.split(
                                '-')
                            each_landlord.contact = "".join(
                                each_landlord.contact)
                            contact_mo = contact.split('-')
                            contact_mo = "".join(contact)
                            if each_landlord.contact == contact_mo:
                                contact_exist_error = True
                                return render(request, 'spaces/signup.html', locals())
                        user = User.objects.create_user(
                            username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                        user.save()
                        landlord = Landlord(user=user, contact=contact)
                        landlord.save()
                    elif not email:
                        for each_landlord in landlords:
                            each_landlord.contact = each_landlord.contact.split(
                                '-')
                            each_landlord.contact = "".join(
                                each_landlord.contact)
                            contact_mo = contact.split('-')
                            contact_mo = "".join(contact)
                            if each_landlord.contact == contact_mo:
                                contact_exist_error = True
                                return render(request, 'spaces/signup.html', locals())
                        user = User.objects.create_user(
                            username=username, first_name=first_name, last_name=last_name, password=password1)
                        landlord = Landlord(user=user, contact=contact)
                        landlord.save()

            elif password1 != password2:
                pass_different_err = True
                return render(request, 'spaces/signup.html', locals())
            return render(request, 'spaces/signin.html', locals())

    context = {'form': form}
    return render(request, 'spaces/signup.html', locals())


def sign_in(request):
    form = SignInForm()
    error = False
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            client_check = form.cleaned_data['client']
            landlord_check = form.cleaned_data['landlord']
            if client_check:
                try:
                    user_tempt = get_object_or_404(User, username=username)
                    client_user = get_object_or_404(
                        Client, user_id=user_tempt.id)
                    if client_user:
                        client_user = authenticate(
                            username=username, password=password)

                        if client_user:
                            login(request, client_user)

                        else:
                            error = True
                except Http404:
                    user_tempt = None
                    error = True

            elif landlord_check:
                try:
                    user_tempt = get_object_or_404(User, username=username)
                    landlord_user = get_object_or_404(
                        Landlord, user_id=user_tempt.id)
                    if landlord_user:
                        landlord_user = authenticate(
                            username=username, password=password)

                        if landlord_user:
                            login(request, landlord_user)
                        else:
                            error = True
                except Http404:
                    user_tempt = None
                    error = True

    return render(request, 'spaces/signin.html', locals())


@login_required()
def see_profile(request, id):
    form = SearchForm()
    user = User.objects.get(id=id)
    try:
        user.is_superuser == 0
        try:
            user.client.user_id != None
            return render(request, 'spaces/see_client_profile.html', locals())
        except:
            user.landlord.user_id != None
            return render(request, 'spaces/see_landlord_profile.html', locals())
    except:
        return render(request, 'spaces/see_profile.html', locals())


@login_required()
def edit_profile(request, id):
    user = User.objects.get(id=id)
    form = EditForm()
    if request.method == 'POST':
        form = EditForm(request.POST , request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['password_verification']
            rent_proposal = form.cleaned_data['rent_proposal']
            deposit_proposal = form.cleaned_data['deposit_proposal']
            avatar = request.FILES.get('avatar')

        user = User.objects.get(id=id)
        try:
            if avatar:
                try:
                    user.client.user_id != None
                    client = Client.objects.get(user_id = id)
                    client.avatar = avatar
                    client.save()
                    avatar_added = True
                except:
                    user.landlord.user_id != None
                    landlord = Landlord.objects.get(user_id = id)
                    landlord.avatar = avatar
                    landlord.save()
                    avatar_added= True
            else:
                avatar_added_err = True
            if username:
                user.username = username
                yes_username_msg = True
            else:
                no_username_msg = True
            if first_name:
                user.first_name = first_name
                yes_first_name_msg = True
            else:
                no_first_name_msg = True
            if last_name:
                user.last_name = last_name
                yes_last_name_msg = True
            else:
                no_last_name_msg = True

            if email:
                user.email = email
                yes_email_msg = True
            else:
                no_email_msg = True
            if contact:
                try:
                    user.client.user_id != None
                    if is_valid_contact(contact) == False:
                        invalid_contact_err = True
                        return render(request, 'spaces/edit_profile.html', locals())
                    client = Client.objects.get(user_id = id)
                    client.contact = contact
                    client.save()

                except:
                    user.landlord.user_id != None
                    if is_valid_contact(contact) == False:
                        invalid_contact_err = True
                        return render(request, 'spaces/edit_profile.html', locals())
                    landlord = Landlord.objects.get(user_id = id)
                    landlord.contact = contact
                    landlord.save()
                yes_contact_msg =   True
            else:
                no_contact_msg = True
            if password1 and password2:
                if password1 == password2:
                    user.set_password(password1)
                    yes_pass_msg = True
                else:
                    error_pass_no_match = True
            else:
                no_pass_msg = True
            user.save()
        except:
            error = True

    return render(request, 'spaces/edit_profile.html', locals())


def add_house(request, id):
    form = AddHouseForm()
    if request.method == 'POST':
        form = AddHouseForm(request.POST, request.FILES)
        if form.is_valid():
            house_township = form.cleaned_data['house_township']
            house_area = form.cleaned_data['house_area']
            house_rent = form.cleaned_data['house_rent']
            house_deposit = form.cleaned_data['house_deposit']
            house_kind = form.cleaned_data['house_kind']
            house_rooms_number = form.cleaned_data['house_rooms_number']
            house_available = form.cleaned_data['house_available']
            house_to_sell = form.cleaned_data['house_to_sell']
            house_image = request.FILES['house_image']

            #house_image = resize(houses_path , house_image)

            landlord = Landlord.objects.get(user_id=id)
            house = House(landlord=landlord, house_area=house_area, house_rent=house_rent, house_deposit=house_deposit,
                          house_kind=house_kind, house_rooms_number=house_rooms_number,
                          house_available=house_available, house_to_sell=house_to_sell, house_image=house_image, house_township=house_township)

            house.save()

    return render(request, 'spaces/add_house.html', locals())


def log_out(request):
    logout(request)
    return redirect(reverse("spaces:signin"))

def see_houses(request , id):
    houses = House.objects.filter(landlord__user_id = id)
    if houses:
        no_house_err = False
    else:
        no_house_err = True
    return render(request ,'spaces/see_houses.html' , locals())

"""
def test(id, username=None, first_name=None, last_name=None, email=None, contact=None, password1=None, password2=None, ):
    user = User.objects.get(id=id)
    try:
        if username:
            user.username = username
            print(user.username)
        else:
            no_username_msg = True
            print("username not changed")
        if first_name:
            user.first_name = first_name
        else:
            no_first_name_msg = True
            print("first name not changed")
        if last_name:
            user.last_name = last_name
        else:
            no_last_name_msg = True
            print("last name not changed")
        if email:
            user.email = email
        else:
            no_email_msg = True
            print("email not changed")
        if contact:
            try:
                user.client.user_id != None
                user.client.contact = contact
            except:
                user.landlord.user_id != None
                user.landlord.contact = contact
        else:
            no_contact_msg = True
            print("contact not changed")
        if password1 and password2:
            if password1 == password2:
                user.set_password(password1)
            else:
                error_pass_no_match = True
        else:
            no_pass_msg = True
            print("no password changed")
        user.save()
    except:
        error = True
"""

def test2(id):
    try:
        houses = House.objects.filter(landlord__user_id = id)
    except:
        error = True 
        print(error)
    