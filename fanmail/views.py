from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FanMail
from .models import PackageNotification
from .forms import FanMailForm
from .forms import PackageNotificationForm
from django.http import JsonResponse

@login_required
def fanmail_list(request):
    fanmails = FanMail.objects.filter(user=request.user)
    return render(request, "fanmail/fanmail_list.html", {"fanmails": fanmails})

@login_required
def fanmail_create(request):
    if request.method == "POST":
        form = FanMailForm(request.POST, request.FILES)
        if form.is_valid():
            fanmail = form.save(commit=False)
            fanmail.user = request.user
            fanmail.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True})
            return redirect("fanmail_list")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": "Invalid form data."}, status=400)
    else:
        form = FanMailForm()
    
    return render(request, "fanmail/fanmail_form.html", {"form": form})

@login_required
def fanmail_update(request, pk):
    fanmail = get_object_or_404(FanMail, pk=pk, user=request.user)
    if request.method == "POST":
        form = FanMailForm(request.POST, request.FILES, instance=fanmail)  
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True})
            return redirect("fanmail_list")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": "Invalid form data."}, status=400)
    else:
        form = FanMailForm(instance=fanmail)
    return render(request, "fanmail/fanmail_form.html", {"form": form})

@login_required
def fanmail_delete(request, pk):
    fanmail = get_object_or_404(FanMail, pk=pk, user=request.user)
    if request.method == "POST":
        fanmail.delete()
        return redirect("fanmail_list")
    return render(request, "fanmail/fanmail_confirm_delete.html", {"fanmail": fanmail})

@login_required
def fanmail_gallery(request):
    fanmails = FanMail.objects.filter(user=request.user, image__isnull=False).exclude(image="")
    return render(request, "fanmail/fanmail_gallery.html", {"fanmails": fanmails})

@login_required
def package_notify(request):
    if request.method == 'POST':
        form = PackageNotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.user = request.user
            notification.save()
            return redirect('fanmail_list')
    else:
        form = PackageNotificationForm()
    return render(request, 'fanmail/package_notify.html', {'form': form})

@login_required
def my_packages(request):
    packages = PackageNotification.objects.filter(user=request.user).order_by('-sent_date')
    return render(request, 'fanmail/my_packages.html', {'packages': packages})