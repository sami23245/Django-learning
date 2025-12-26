from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("<h1>Welcome to the new Django project!</h1>")
    people = [
        {"name": "Samis", "age": 20},
        {
            "name": "John", "age": 25
        },
        {
            "name": "Doe", "age": 30
        },
    ]
    return render(request, "index.html", context={"people": people})
def about(request):
    return HttpResponse("<h1>About Us</h1><p>This is the about page of our Django project.</p>")
