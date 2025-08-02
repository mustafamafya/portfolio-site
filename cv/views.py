from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')  # Ensure the user is logged in to access the profile
def cv(request):
    return render(request, 'cv.html', {})