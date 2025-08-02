from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Custom user creation form
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput )
    
     

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name', 'address', 'phone_number',
            'city', 'zip_code', 'country', 'profile_picture'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Address', 'style': 'resize:none;'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

