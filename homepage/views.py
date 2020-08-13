from django.shortcuts import render


# Create your views here.
def h(request):
    return render(request, "homepage/homepage.html", {})


def about(request):
    return render(request, 'timezone/about.html', {})
