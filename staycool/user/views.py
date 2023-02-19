from django.shortcuts import render
from django.http import HttpRequest


def signin_view(request):
    return render(request, 'signin.html')


def signup_view(request):
    return render(request, 'signup.html')


