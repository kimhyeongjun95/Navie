from django.shortcuts import render, redirect
from accounts.forms import SignUpForm, SearchIdForm, SearchPasswordForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
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
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


# def search_info(request):
#     if request.user.is_authenticated:
#         return redirect('movies:index')
    
#     if request.method == 'GET':
#         search_id_form = SearchIdForm(request.GET)
#         search_password_form = SearchPasswordForm(request.GET)
#         if search_id_form.is_valid() and search_id_form.name
#     return render(request, 'accounts/search_info.html')

# @login_required
# @require_http_methods(['GET', 'POST'])
# def update(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     context = {
#         'form':form,
#     }
#     return render(request, 'accounts/update.html', context)


# @require_POST
# def delete(request):
#     if request.user.is_authencated:
#         request.user.delete()
#         auth_logout(request)
#     return redirect('articles:index')


# @login_required
# @require_http_methods(['GET', 'POST'])
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('articles:index')
#     else:
#         form = PasswordChangeForm(request.user)
#     context = {
#         'form':form,
#     }
#     return render(request, 'accounts/change_password.html', context)