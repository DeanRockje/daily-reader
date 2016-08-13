from rest_framework import serializers
from feed.models import Feed, Entry, Category
from django.contrib.auth.models import User


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            'id','url','title','publication_date'
        )


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'link','title','was_read','publication_date','content'
        )


