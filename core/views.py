from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Electroshop API - Your e-commerce backend")
