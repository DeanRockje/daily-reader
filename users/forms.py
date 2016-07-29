from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError('User does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Password incorrect')
        if not user.is_active():
            raise forms.ValidationError('Users account disabled')
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')

        user = User.objects.get(username = username)

        if user is not None:
            raise forms.ValidationError('User with such username exists')
        return self.cleaned_data