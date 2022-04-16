from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm,newHoodForm, PostForm, BusinessForm,ServiceForm,ProfileForm
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

# details
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    if request.method == "POST":
        hood_group = HoodMember.objects.filter(member=current_user).first()
        hood = hood_group.hood
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.neighborhood = hood
            post.save()
            messages.success(request,('Posted!'))
            return redirect('home')
    else:
        hood_group = HoodMember.objects.filter(member=current_user).first()
        if hood_group is not None:
            hood = hood_group.hood
            posts =Post.objects.filter(neighborhood =hood)
            form = PostForm()
            context = {
                'hood':hood,
                'posts':posts,
                'form':form,
            }
            return render(request,'home.html', context)
        else:
            return redirect('dashboard')
#new neighborhood
@login_required(login_url='/accounts/login/')
def new_hood(request):
    if request.method == 'POST':
        current_user = request.user
        form = newHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.creator = current_user
            hood.save()
            new_member = HoodMember(member=current_user,hood=hood)
            new_member.save()
            messages.success(request,('Neighborhood created!'))
            return redirect('dashboard')
    else:
        form = newHoodForm()
    return render(request,'new-hood.html', {'form':form})
#join neighborhood
@login_required(login_url='/accounts/login/')
def join_hood(request,hood_id):
    hood = get_object_or_404(Neighborhood,id=hood_id)
    member = HoodMember.objects.filter(Neighborhood =hood,member =request.user)
    if member is not None:
        new_member = HoodMember(member = request.user, hood= hood)
        new_member.save()
        messages.success(request,("You've joined the group"))
    else:
        messages.success(request,("You're already a member"))
    return redirect('home')
#leave neighborhood
@login_required(login_url='/accounts/login/')
def leave_hood(request,hood_id):
    current_user = request.user
    hood = get_object_or_404(Neighborhood,id=hood_id)
    membership = HoodMember(member = current_user, hood= hood)
    membership.delete()
    return redirect('dashboard')

