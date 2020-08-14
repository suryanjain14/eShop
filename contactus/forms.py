from django import forms
from django.core import validators


from .models import Message


class ContactForm(forms.ModelForm):
    message = forms.CharField(validators=[validators.MinLengthValidator(4)], widget=forms.Textarea(
        attrs={"class": "form-control w-100", "name": "message",  "cols": "30", "rows": "9",
               "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Message'",
               "placeholder": " Enter Message"}))
    name = forms.CharField(validators=[validators.MaxLengthValidator(20), validators.MinLengthValidator(2)])
    email = forms.EmailField(validators=[validators.EmailValidator()])
    subject = forms.CharField(validators=[validators.MaxLengthValidator(20)])
    name.widget.attrs.update({"class": "form-control valid", "name": "name",  "type": "text",
               "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter your name'",
               "placeholder": "Enter your name"})
    email.widget.attrs.update({"class": "form-control valid", "name": "email",  "type": "email",
               "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter your email'",
               "placeholder": "Enter your email"})
    subject.widget.attrs.update({"class": "form-control valid", "name": "subject",  "type": "text",
               "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter subject'",
               "placeholder": "Enter subject"})

    class Meta:
        model = Message
        fields = ['message', 'name', 'email', 'subject']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validators.validate_email(email)
            valid_email = True
        except validators.validate_email.ValidationError:
            valid_email = False
        if not valid_email:
            raise forms.ValidationError("Invalid Email")

        return email
