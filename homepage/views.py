from django.shortcuts import render


# Create your views here.
def h(request):
    return render(request, "timezone/index.html", {})

def about(reuest):
    return render(reuest , 'timezone/about.html',{})