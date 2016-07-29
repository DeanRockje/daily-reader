from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import feedparser
import datetime
from time import mktime

# Create your models here.


class Category(models.Model):
    category_title = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_set', null=True)


    def __str__(self):
        return "%s" % self.category_title

    def get_category_title(self):
        return self.category_title


class Feed(models.Model):
    url = models.URLField(max_length=100)
    title = models.CharField(max_length=100,blank=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    build_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default = 'no category')

    def get_entry_data(self):
        data = feedparser.parse(self.url)

        for entry in data.entries:
            url = entry.link
            title = entry.title
            pub_date = datetime.datetime.fromtimestamp(mktime(entry.published_parsed))
            build = datetime.datetime.fromtimestamp(mktime(entry.updated_parsed))
            if not hasattr(entry, 'content'):
                content = entry.description
            else:
                content = entry.content
            feed = self
            try:
                Entry.objects.get(link=entry.link)
            except Entry.DoesNotExist:
                entry = Entry(feed=feed, link=url, title=title, content=content, publication_date=pub_date,
                              update_time=build)
                entry.save()

    def save(self, *args, **kwargs):
        parser = feedparser.parse(self.url)
        if not self.title:
            self.title = parser.feed.title
            if not hasattr(parser.feed, 'published_parsed'):
                self.publication_date = timezone.now()
            else:
                self.publication_date = datetime.datetime.fromtimestamp(mktime(parser.feed.published_parsed))
            if not hasattr(parser.feed, 'updated_parsed') or not parser.feed.updated_parsed:
                self.build_date = timezone.now()
            else:
                self.build_date = datetime.datetime.fromtimestamp(mktime(parser.feed.updated_parsed))
            super(Feed, self).save(*args, **kwargs)
            self.get_entry_data()

    def __str__(self):
        return "%s" % self.url


class Entry(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    link = models.URLField(max_length=100,blank=True, default='', null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(null=True,blank=True)
    publication_date = models.DateTimeField(null=True,blank=True)
    update_time = models.DateTimeField(null=True,blank=True )
    was_read = models.BooleanField(blank=True,default=False)

    def set_read(self):
        self.was_read=True
        Entry.save()

    def __str__(self):
        return " %s " % self.title


