# Import necessary Django modules and forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Import custom forms and models
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile

# 🔐 View: Display user profile (requires login)
@login_required(login_url='login')  # Redirects to login if user is not authenticated
def profile(request):
    # Fetch the profile associated with the logged-in user
    user_profile = Profile.objects.get(user=request.user)

    # Render the profile page with profile data and form (for potential editing)
    return render(request, 'profile.html', {
        'profile': user_profile,
        'form': ProfileForm  
    })

# 🔑 View: Handle user login
def login_user(request):
    # Redirect authenticated users to home/dashboard
    if request.user.is_authenticated:
        return redirect('home')

    # Handle login form submission
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('profile')  # Redirect to profile after login
        else:
            messages.error(request, 'Invalid username or password.')

    # Render login form for GET requests or failed login
    return render(request, 'login.html')

# 🆕 View: Handle user registration
def register(request):
    # Redirect authenticated users away from registration
    if request.user.is_authenticated:
        return redirect('home')

    # Initialize empty form or process submitted data
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save new user to database
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login after successful registration

    # Render registration form
    return render(request, 'register.html', {'form': form})

# 🚪 View: Log out the current user
def logout_page(request):
    logout(request)  # Terminate user session
    return redirect('login')  # Redirect to login page

# ✏️ View: Update user profile (requires login)
@login_required
def update_profile(request):
    # Get or create profile for the logged-in user
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    # Handle profile update form submission
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        # Pre-fill form with existing profile data
        form = ProfileForm(instance=user_profile)

    # Render profile update form
    return render(request, 'update_profile.html', {'form': form})

# ❌ View: Delete user profile and account (requires login)
@login_required
def delete_profile(request):
    if request.method == 'POST':
        # Delete profile and user account
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        user = request.user
        logout(request)  # Log out before deleting user
        user.delete()    # Delete user from database

        messages.success(request, 'Your profile has been deleted.')
        return redirect('register')  # Redirect to registration page

    # Fallback redirect if accessed via GET
    return redirect('profile')