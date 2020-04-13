from django.shortcuts import render,redirect
from s_admin.models import AdminLoginModel
from django.contrib import messages

def admin_login(request):
    return render(request,"s_admin/login.html")


def admin_login_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername,password=apassword)
        request.session['status'] = True
        return redirect('admin_home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request,"Sorry Invalid Details")
        return redirect('admin_login')


def admin_home(request):
    return render(request, "s_admin/admin_home.html")


def admin_logout(request):
    request.session['status'] = False
    return redirect('admin_login')