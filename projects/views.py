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
#search by location
def search_hood(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        print(search_term)
        hoods = Neighborhood.search_hood(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{'hoods':hoods})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


