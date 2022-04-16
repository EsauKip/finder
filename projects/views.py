from django.shortcuts import render
from django.http import HttpResponse

from .models import Neighborhood, Post, Profile, HoodMember,Business,Service
def index(request):
    return render(request, 'index.html')

#show neighborhood
def dashboard(request):
    hoods=Neighborhood.objects.all()
    context={'hoods':hoods}
    return render(request,'dashboard.html',context)