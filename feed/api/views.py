from feed.models import Feed, Entry, Category
from .serializers import FeedSerializer, EntrySerializer, CategorySerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.contrib.auth.models import User

class FeedAPI(APIView):

    def get(self,request,format=None):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)


class FeedAPIdetailed(APIView):

    def get_object(self,pk):
        try:
            feed = Feed.objects.get(id=pk)
        except Feed.DoesNotExist:
            raise Http404
        return feed

    def get(self, request, pk, format=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        feed = self.get_object(pk)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk,formt=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPIdetailed(APIView):
    def get_object(self,pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404
        return category

    def delete(self,pk,request,fomat=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,pk,request,format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk,format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategoryAPI(APIView):

    def get(self,request,fomat=None):
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)


class EntryAPIdetailed(APIView):
    def get_object(self,pk):
        try:
            entry = Entry.objects.get(id=pk)
        except Entry.DoesNotExist:
            raise Http404
        return entry

    def get(self,request,pk,format=None):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)


class UserAPI(APIView):
    def get(self,request,format=None):
        user = User.objects.all()
        serializer= UserSerializer(user)
        return Response(serializer.data)