from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def signup(request):
    return render(request, 'authentication/signup.html')

def signin(request):
    return render(request, 'authentication/signin.html')