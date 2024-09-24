
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Home Page!")

def wwe_view(request):
    return HttpResponse("Welcome to WWE Page")
