import datetime
from http.client import HTTPResponse

from django.contrib import auth, messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from . import models


# Create your views here.
def Home(r):
    if not r.user.is_authenticated:
        return redirect('/login')
    return render(r, 'home.html', {'status': "home"})


def Login(r):
    if r.method == 'POST':
        username = r.POST['username']
        password = r.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(r, user)
            messages.success(r, 'Login Successfull')
            return redirect('/')
    return render(r, 'login.html')


def Logout(r):
    logout(r)
    messages.success(r, 'Logout Successfully')
    return redirect('/login')


def TrackAWB(r):
    if not r.user.is_authenticated:
        return redirect('/login')
    awbno = r.GET['awb_no']
    bookingdata = models.BookingData.objects.filter(awbno=awbno)
    transitdata = models.TransitDetails.objects.filter(awbno=awbno)
    if bookingdata:
        return render(r, 'home.html',
                      context={"book": bookingdata, 'trans': transitdata, 'status': 'track', 'awbno': awbno,
                               'dest': models.Destinations.objects.all(), 'pcs': bookingdata[0].pcs,
                               'wt': bookingdata[0].wt, 'date': bookingdata[0].date})
    else:
        messages.error(r, 'No Data Found')
        return redirect('/')


def AddActivity(r):
    if not r.user.is_authenticated:
        return redirect('/login')
    if r.method == 'POST':
        date = r.POST['date']
        station = r.POST['station']
        activity = r.POST['activity']
        awbno = r.POST['awbno']
        models.TransitDetails.objects.create(date=date, station=station, activitylist=activity, awbno=awbno)
        messages.success(r, 'Added Successfully')
        return redirect(f'/track-awb/?awb_no=' + awbno)


def AddShipment(r):
    if not r.user.is_authenticated:
        return redirect('/login')
    if r.method == 'POST':
        reciever_name = r.POST['reciever_name']
        reciever_phone = r.POST['reciever_phone']
        reciever_address = r.POST['reciever_address']
        reciever_station = r.POST['reciever_station']
        sender_name = r.POST['sender_name']
        sender_phone = r.POST['sender_phone']
        sender_address = r.POST['sender_address']
        sender_station = r.POST['sender_station']
        awbno = r.POST['awbno']
        pcs = r.POST['pcs']
        wt = r.POST['wt']
        date = r.POST['date']
        models.BookingData.objects.create(sender_name=sender_name, sender_address=sender_address,
                                          sender_station=sender_station, sender_phone=sender_phone,
                                          reciever_name=reciever_name, reciever_phone=reciever_phone,
                                          reciever_station=reciever_station, reciever_address=reciever_address,
                                          awbno=awbno, pcs=pcs, wt=wt, date=date)
        models.TransitDetails.objects.create(date=datetime.date.today(), station=sender_station, activitylist='Booked',
                                             awbno=awbno)
        messages.success(r, "Added Successfully")
        return redirect('/')
    return render(r, 'addship.html', {'dest': models.Destinations.objects.all()})


def track(r):
    if r.method == 'POST':
        awbno = r.POST['awb_no']
        bookingdata = models.BookingData.objects.filter(awbno=awbno)
        transitdata = models.TransitDetails.objects.filter(awbno=awbno)
        if bookingdata:
            return render(r, 'track.html',
                          context={"book": bookingdata, 'trans': transitdata, 'status': 'track', 'awbno': awbno,
                                   'dest': models.Destinations.objects.all(), 'pcs': bookingdata[0].pcs,
                                   'wt': bookingdata[0].wt, 'date': bookingdata[0].date})
        else:
            messages.error(r, 'No Data Found')

    return render(r, 'track.html', {'status': "home"})
