from django import forms
from .models import Feed, Category, User
from django.contrib.auth import get_user_model, authenticate
from django.core import exceptions
import feedparser


class AddFeed(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['url','category']

    def clean(self):
        feed_url = self.cleaned_data.get('url')
        parser = feedparser.parse(feed_url)
        if parser.bozo == 1:
            raise forms.ValidationError('The link contains no rss feeds or feed XML badly formatted')
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


