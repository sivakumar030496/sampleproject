from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import *
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.
def index(request):
    context = {
        "home":"home"
    }
    return render(request,'index.html',context)
def about_us(request):
    return render(request,'aboutus.html')
def home(request):
    return render(request,'home')
def profiles(request):
    profile_obj=profile.objects.all()
    context={'profile_obj':profile_obj}
    return render(request,'profiles.html',context)
def privacy_policy(request):
    return render(request,'privacy_policy.html')
def terms_conditions(request):
    return render(request,'terms_conditions')
def annoucement(request):
    return render(request,'announcement')
def contactus(request):
    return render(request,'contactus')
def profile_view(request,slug):
    profile_view_obj=profile.objects.get(name=slug)
    context={'profile_view_obj':profile_view_obj}

    return render(request,'profile_view.html',context)

def get_profile_view(request):
    print(request.POST)
    if request.method == 'POST' and request.is_ajax():
        print('warning')
        start_count=int(request.POST.get('start_count'))
        end_count=int(request.POST.get('end_count'))
        profile_count=profile.objects.all().count()
        if profile_count >= end_count:
            profile_count=profile.objects.all().order_by('id')[(int(start_count)-1):end_count]
            print(profile_obj)
            latest_count = (1+ end_count)
            data = serializers.serialize('json',profile_obj,fields=('name','profile_image'))
            return JsonResponse({'status':'success','latest_count':latest_count,'profile_obj':data},status=200)
        else:
            return JsonResponse({'status':'success','latest_count':latest_count,'profile_obj':data},status=200)
    print('cool')
    return JsonResponse(({'status':'fields'},),status=400)

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            return redirect('about_us')
        return render(request,'login.html')


