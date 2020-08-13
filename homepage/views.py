from django.shortcuts import render


# Create your views here.
def h(request):
    return render(request, "timezone/index.html", {})


def about(request):
    return render(request, 'timezone/about.html', {})
