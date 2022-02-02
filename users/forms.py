from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from .models import *

class SignUpForm(UserCreationForm):
    username = UsernameField(
        min_length=5, max_length=20,
        label='아이디',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    # username = forms.CharField(min_length=5, max_length=20, label="아이디")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2", "name", "tel")
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.name = self.cleaned_data["name"]
        user.tel = self.cleaned_data["tel"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        min_length=5, max_length=20,
        label='아이디',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label=_("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    error_messages = {
        'invalid_login': _(
            "올바른 아이디와 비밀번호를 입력하세요."
        ),
        'inactive': _("비활성화된 계정입니다."),
    }

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         labels = {
#             'username': _('아이디'),
#             'password': _('비밀번호'),
#         }