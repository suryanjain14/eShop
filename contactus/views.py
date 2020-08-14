from django.shortcuts import render,redirect,HttpResponse
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
           return HttpResponse("<h1>Check your form </h1>")
    else:
        form = ContactForm()
        return render(request, 'contactus/contact.html', {'form':form})