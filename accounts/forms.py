from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model


username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    name = forms.CharField(
        label='이름',
        max_length=20,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'accounts-name input_area',
            })
    )

    username = forms.CharField(
        label='아이디',
        max_length=30,
        help_text=_(''), # 30자 이내 문자, 숫자, 특수문자(@ . + -)만 가능
        validators=[username_validator],
        error_messages={'unique': _("이미 존재하는 아이디입니다.")},
        widget=forms.TextInput(attrs={
            'class': 'accounts-id input_area',
            })
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={
            'class': 'accounts-password input_area',
            }),
        error_messages={'invalid': _("최소 8자 이상의 문자와 숫자로 이루어진 비밀번호를 입력해주세요.")},
        # help_text=password_validation.password_validators_help_text_html()
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'accounts-passwordconfirm input_area',
                }),
        help_text=_('')
    )

    email = forms.EmailField(
        label='이메일',
        max_length=50,
        help_text=_(''),
        widget=forms.TextInput(attrs={
            'class': 'accounts-email input_area',
            })
    )

    class Meta:
        model = get_user_model()
        fields = ('name', 'username', 'password1', 'password2', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
    

class SearchIdForm(forms.Form):
    name_id = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={
            'class': 'accounts-search_id-name',
            'placeholder': '이름',
        })
    )

    email_id = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={
            'class': 'accounts-search_id-email',
            'placeholder': '이메일',
        })
    )

class SearchPasswordForm(forms.Form):
    username_password = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={
            'class': 'accounts-search_password-id',
            'placeholder': '아이디',
        })
    )

    name_password = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={
            'class': 'accounts-search_password-name',
            'placeholder': '이름',
        })
    )

    email_password = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={
            'class': 'accounts-search_password-email',
            'placeholder': '이메일',
        })
    )