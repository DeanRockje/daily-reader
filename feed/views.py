from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Feed,Entry,Category
from .forms import AddFeed, CreateCategory
from django.contrib.auth.decorators import login_required
from .tasks import update_feed


# Create your views here.

@login_required
def category_index(request):
    user = request.user
    category_list = user.category_set.all()
    return render(request, 'feed/category.html', {'category_list':category_list})

@login_required
def feed_list(request,pk):
    feeds = Feed.objects.filter(category__id = pk).order_by('-adding_date')
    return render(request,'feed/feed_list.html', {'feed':feeds})

@login_required
def entry_list(request,pk):
    entries = Entry.objects.filter(feed__id=pk).order_by('-publication_date')
    return render(request,'feed/feed_items.html',{'entry':entries})

@login_required
def add_feed(request):
    if request.method == 'POST':
        form = AddFeed(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.save()
            return HttpResponseRedirect('/digest/')
    else:
        form=AddFeed()
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'feed/add_feed.html', {'form':form})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CreateCategory(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return HttpResponseRedirect('/digest/')
    else:
        form = CreateCategory()
    return render(request, 'feed/add_category.html', {'form':form})


@login_required
def manual_refresh(request, pk):
    feed = Feed.objects.get(pk=pk)
    update_feed(feed).delay()
    entries = Entry.objects.filter(feed__id = pk)
    return render(request,'feed/entry_list.html',{'entries':entries})