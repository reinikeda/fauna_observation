from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from . import forms, models


User = get_user_model()

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_error = False
        if len(password1) == 0 or password1 != password2:
            is_error = True
            messages.error(request, _('password do not match or were not entered'))
        if len(username) == 0 or User.objects.filter(username=username).exists():
            is_error = True
            messages.error(request, _('username already taken or was not entered'))
        if len(email) == 0 or User.objects.filter(email=email).exists():
            is_error = True
            messages.error(request, _('user with this email already exists, or email was not entered'))
        if not is_error:            
            try:
                User.objects.create_user(username=username, email=email, password=password1)
            except Exception as e:
                is_error = True
                messages.error(request, str(e))
        if not is_error:
            messages.success(request, f'{_("user")} {username} {_("has been succesfully registered, you can log in now")}')
            return redirect(reverse_lazy('login'))
    return render(request, 'user_profile/register.html')

@login_required
def detail_active(request):
    return render(request, 'user_profile/detail.html', {
        'object': request.user.profile
    })

def detail(request, username):
    return render(request, 'user_profile/detail.html', {
        'object': get_object_or_404(models.Profile, user__username=username)
    })

@login_required
def update(request):
    if request.method == "POST":
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        profile_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('your profile was successfully updated'))
            return redirect('profile_detail_active')
    else:
        user_form = forms.UserUpdateForm(instance=request.user)
        profile_form = forms.ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user_profile/update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })