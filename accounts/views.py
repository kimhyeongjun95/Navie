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
        try:
            print(search)
            u1 = get_user_model().objects.get(name=search.get('name_id'))
            print(u1)
            u2 = get_user_model().objects.get(email=search.get('email_id'))
            print(u2)
            users1 = get_user_model().objects.filter(name=search.get('name_id'))
            users2 = get_user_model().objects.filter(email=search.get('email_id'))
            print(users1, '1')
            print(users2, '2')
            for user1 in users1:
                print(user1)
                for user2 in users2:
                    print(user2)
                    if user1.pk == user2.pk:
                        return redirect('accounts:searched_id', user1.pk)
            else:
                return redirect('accounts:search_info')
        except:
            try:
                users3 = get_user_model().objects.filter(username=search.get('username_password'))
                users4 = get_user_model().objects.filter(name=search.get('name_password'))
                print(users3, '3')
                print(users4, '4')
                for user3 in users3:
                    for user4 in users4:
                        if user3.pk == user4.pk:
                            return redirect('/accounts/password/reset/')
                else:
                    return redirect('accounts:search_info')
            except:
                return redirect('accounts:search_info')

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
            try:
                user.image = request.FILES['image']
                user_change_form.save()
                return redirect('accounts:profile', user.username)
            except:
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