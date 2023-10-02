from crypt import methods
from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Visitor, OwnerList, RoomData, BookingData
from .forms import RoomDataForm
# Create your views here.
def index(request):
    group_name = request.user.groups.values_list('name',flat = True)
    if 'Owner' in group_name:
        username = request.user.username
        data = BookingData.objects.filter(owner=username).values()
        print(data)
        return render(request, 'dashboard/index.html',{'data':data})
    else:
        return redirect("./login")

def CreateUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = OwnerList(name=name, phone=phone, email=email)
        data.save()
        user = User.objects.create_user(email, email, password)
        my_group = Group.objects.get(name='Owner') 
        my_group.user_set.add(user)
        user.save()
        return redirect("./")
    else:
        return render(request, 'login.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect("./")
        else:
            return redirect('./login')
    else:
        if request.user.is_authenticated:
            group_name = request.user.groups.values_list('name',flat = True)
            if 'Owner' in group_name:
                return redirect("./")
            else:
                return redirect('/')
        else:    
            return render(request, 'login.html')


def room(request):
    group_name = request.user.groups.values_list('name',flat = True)
    if 'Owner' in group_name:
        username = request.user.username
        data = RoomData.objects.filter(updated_by=username).values()
        data = {'data':data}
        print(data)
        return render (request, 'dashboard/room.html', data)
    else:
        return redirect('./login')

def add_room(request):
    group_name = request.user.groups.values_list('name',flat = True)
    if 'Owner' in group_name:
        if request.method == 'POST':
            form = RoomDataForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Redirect to a success page or do something else
                return redirect("./")
            else:
                return HttpResponse("Form is incorect")
        else:
            form = RoomDataForm()
        username = request.user.username
        return render(request, 'dashboard/add_room.html', {'form': form, "username":username})
        # return render(request, 'dashboard/add_room.html')
    else:
        return redirect("./login")

def CustomLogout(requst):
    logout(request)
    return redirect('/')

def profile(request):
    group_name = request.user.groups.values_list('name',flat = True)
    if 'Owner' in group_name:
        username = request.user.username
        userdata = OwnerList.objects.filter(email=username).values()
        bookking = BookingData.objects.filter(email=username).values()
        data = {'userdata':userdata, 'bookking':bookking}
        # print(data)
        return render(request, 'dashboard/profile.html', data)
    else:
        return redirect('/login')
    
def edit(request, pid):
    pid = int(pid)
    group_name = request.user.groups.values_list('name',flat = True)
    
    if 'Owner' in group_name:
        if request.method =="POST":
            title = request.POST.get('title')
            room_id = request.POST.get('room_id')
            floor = request.POST.get('floor')
            bed = request.POST.get('bed')
            bathroom = request.POST.get('bathroom')
            location = request.POST.get('location')
            about = request.POST.get('about')
            desc = request.POST.get('desc')
            prize = request.POST.get('prize')
            wifi = request.POST.get('wifi')
            RoomData.objects.filter(room_id=room_id).update(
                title=title, floor=floor, bed=bed, bathroom=bathroom, location=location,
                about=about, desc=desc, prize=prize, wifi=wifi)
            return redirect('/room')
        else:
            room_data = RoomData.objects.filter(id=pid).values()
            username = request.user.username
            return render(request, 'dashboard/edit_room.html', {'username':username, 'room_data':room_data})
    else:
        return redirect("/login")