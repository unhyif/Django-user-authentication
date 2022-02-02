from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *

class SignUpForm(UserCreationForm):
    username = UsernameField(
        min_length=5, max_length=20,
        label='아이디',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
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


class LoginForm(forms.Form):
    username = UsernameField(
        min_length=5, max_length=20,
        label='아이디',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='비밀번호', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=username) 
            if user.check_password(password):
                return self.cleaned_data
            else:
                raise forms.ValidationError("올바른 비밀번호를 입력하세요.")
        except User.DoesNotExist:
            raise forms.ValidationError("입력하신 아이디와 일치하는 계정이 없습니다.")