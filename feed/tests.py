from django.test import TestCase
from .forms import AddFeed,CreateCategory
from .models import Category, User

class TestFeed(TestCase):
    def test_valid(self):
        url = "https://habrahabr.ru/rss/hub/programming/"
        user = User.objects.create(username='Dean', password='DeanRocje', email='email@email.com')
        category = Category.objects.create(category_title='News',user=user)
        form = AddFeed({
            'url':url,
            'category_title':category
        })

        self.assertEqual(form.is_valid(),True, msg="Form is valid")

    def test_category_add(self):
        form = CreateCategory({
            'category_title':'bla bla',
            'user':User.objects.get(id=1)
        })

        self.assertTrue(form.is_valid())