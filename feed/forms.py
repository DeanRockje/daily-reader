from django import forms
from .models import Feed, Category, User
from django.contrib.auth import get_user_model, authenticate
from django.core import exceptions


class AddFeed(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['url','category']

    def clean(self):
        feed_url = self.cleaned_data.get('url')
        try:
            feed = Feed.objects.get(url=feed_url)
            raise forms.ValidationError('Feed already exists')
        except Feed.DoesNotExist:
            pass
        return self.cleaned_data


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields=['category_title']

    def clean(self):
        title = self.cleaned_data.get('category_title')
        try:
            category = Category.objects.get(category_title = title)
            raise forms.ValidationError('Category already exists')
        except Category.DoesNotExist:
            pass
        return self.cleaned_data


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

        if username is None or password is None or email is None:
            raise forms.ValidationError('Please, correct the errors below')
        return self.cleaned_data