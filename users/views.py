from django.shortcuts import render, redirect
from .forms import UserProfileCreationForm 

def signup_view(request):
    if request.method == "POST":
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserProfileCreationForm()
    return render(request, "registration/signup.html", {"form": form})
