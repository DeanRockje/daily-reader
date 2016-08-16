from rest_framework import serializers
from feed.models import Feed, Entry, Category
from django.contrib.auth.models import User

# I have to DELETE data, CREATE data, GET data, UPDATE

class FeedSerializer(serializers.ModelSerializer):
    entries = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = Feed
        fields = (
            'category', 'id','url','title','publication_date','entries'
        )


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'link','title','was_read','publication_date','content'
        )


class CategorySerializer(serializers.ModelSerializer):
    feeds = serializers.StringRelatedField(many=True)
    user =serializers.StringRelatedField()
    class Meta:
        model = Category
        fields=(
            'id','user','category_title','feeds'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','name'
        )