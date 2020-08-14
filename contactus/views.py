from django.shortcuts import render,redirect,HttpResponse
from .forms import ContactForm

# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'contactus/contact.html', {'form':form})