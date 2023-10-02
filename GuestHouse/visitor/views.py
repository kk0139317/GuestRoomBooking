from crypt import methods
from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from owner.models import Visitor
from owner.models import Contact, RoomData, BookingData


def index(request):
    roomdata =  RoomData.objects.all()
    roomdata={"roomdata":roomdata}
    return render (request,'index.html', roomdata)

def about(request):
    return render (request,'about.html')

def service(request):
    return render (request, 'service.html')

def rooms(request):
    roomdata =  RoomData.objects.all()
    roomdata={"roomdata":roomdata}
    return render (request, 'room.html', roomdata)

def booking(request, pid):

    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        room_id = request.POST.get("room_id")
        title = request.POST.get("title")
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        adult = request.POST.get("adult")
        chield = request.POST.get("chield")
        message = request.POST.get("message")
        owner = request.POST.get('owner')

        data = BookingData(name=name, email=email, room_id=room_id, owner=owner, 
                        title=title, checkin= checkin, checkout=checkout,
                        adult=adult, chield=chield, message=message)
        data.save()
        return redirect("./")
    else:

        pid = int(pid)
        room_data = RoomData.objects.filter(id=pid).values()
        username = request.user.username
        userdata = Visitor.objects.filter(email=username).values()
        data = {"room_data":room_data, 'userdata':userdata}
        print(username, userdata)
        return render (request, 'booking.html', data)

def contact(request):
    if request.method =="POST":
        group_name = request.user.groups.values_list('name',flat = True)
        if 'Visitor' in group_name:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            data = Contact(name=name, email=email, subject=subject, message=message)
            data.save()
            return redirect("./")
        else:
            return redirect("/login")
    else:

        return render (request, 'contact.html')


def CreateUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = Visitor(name=name, phone=phone, email=email)
        data.save()
        user = User.objects.create_user(email, email, password)
        my_group = Group.objects.get(name='Visitor') 
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
            return redirect("/")
        else:
            return redirect('./login')
    else:
        if request.user.is_authenticated:
            return redirect("./")
        else:    
            return render(request, 'login.html')

def profile(request):
    group_name = request.user.groups.values_list('name',flat = True)
    if 'Visitor' in group_name:
        username = request.user.username
        userdata = Visitor.objects.filter(email=username).values()
        bookking = BookingData.objects.filter(email=username).values()
        data = {'userdata':userdata, 'bookking':bookking}
        # print(data)
        return render(request, 'profile.html', data)
    else:
        return redirect('/login')