from django import forms
from .models import CustomUser  # Replace with your actual model

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_photo']  # Adjust fields as needed

# Example of a custom form (not tied to a model)
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ExampleForm(forms.Form):
    # Define your form fields here
    field_name = forms.CharField(max_length=100)
