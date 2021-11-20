from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import SignUpForm, SearchIdForm, SearchPasswordForm, UserInfoChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model, login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        signup_form = SignUpForm()
    context = {
        'signup_form':signup_form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    return render(request, 'accounts/login.html')


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def search_info(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        search = request.POST
        print(search)
        try:
            print(search.get('name_id'))
            print(search.get('email_id'))
            user1 = get_object_or_404(get_user_model(), name=search.get('name_id'))
            user2 = get_object_or_404(get_user_model(), email=search.get('email_id'))
            if user1.pk == user2.pk:
                return redirect('accounts:searched_id', user1.pk)
        except:
            print(search.get('username_password'))
            print(search.get('name_password'))
            print(search.get('email_password'))
            user3 = get_object_or_404(get_user_model(), username=search.get('username_password'))
            user4 = get_object_or_404(get_user_model(), name=search.get('name_password'))
            user5 = get_object_or_404(get_user_model(), email=search.get('email_password'))
            if user3.pk == user4.pk == user5.pk:
                return redirect('accounts:search_change_password', user3.pk)
    search_id_form = SearchIdForm()
    search_password_form = SearchPasswordForm()
    context = {
        'search_id_form': search_id_form,
        'search_password_form': search_password_form,
    }
    return render(request, 'accounts/search_info.html', context)


@require_safe
def searched_id(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/searched_id.html', context)


@require_http_methods(['GET', 'POST'])
def search_change_password(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        password_change_form = SetPasswordForm(user, request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('accounts:login')
    else:
        password_change_form = SetPasswordForm(user)
    context = {
        'user': user,
        'password_change_form':password_change_form,
    }
    return render(request, 'accounts/search_change_password.html', context)


@require_safe
def profile(request, user_username):
    person = get_object_or_404(get_user_model(), username=user_username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_personal_info(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        user_change_form = UserInfoChangeForm(request.POST, request.FILES, instance=user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:profile', user.username)
    else:
        user_change_form = UserInfoChangeForm(instance=user)
    context = {
        'user': user,
        'user_change_form': user_change_form,
    }
    return render(request, 'accounts/change_personal_info.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(request.user, request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            return redirect('movies:index')
    else:
        change_password_form = PasswordChangeForm(request.user)
    context = {
        'change_password_form': change_password_form,
    }
    return render(request, 'accounts/change_password.html', context)


@require_POST
def delete_user(request, user_pk):
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), pk=user_pk)
        user.delete()
    return redirect('movies:index')