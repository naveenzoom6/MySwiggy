from django.shortcuts import render,redirect
from restaurant.forms import *
from django.contrib import messages


def showMain(request):
    return render(request,"restaurant/main.html")


def registerPage(request):
    return render(request,"restaurant/register.html",{"rf":RestaurantForm()})


def save_res(request):
    rf = RestaurantForm(request.POST)
    if rf.is_valid():
        db = rf.save(commit=False)
        db.restro_otp = 5475
        db.restro_status = 'pending'
        db.save()
        messages.success(request,"Once the admin approve the Registration you will receive an email and a text Message")
        return redirect('restro')
    else:
        return render(request,"restaurant/register.html",{"rf":rf})