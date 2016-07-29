from django.contrib import admin
from .models import Feed, Entry, Category
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_title')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset == 'Category':
            instances = formset.save(commit = False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(user=request.user)

# Register your models here.

admin.site.register(Feed)
admin.site.register(Entry)
admin.site.register(Category)
