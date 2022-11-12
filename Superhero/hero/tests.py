from django.test import SimpleTestCase, TestCase

from .models import Article


class BlogAppTest(SimpleTestCase):
    def test_django(self):
        self.assertTrue(True)


class BlogDataTest(TestCase):
    def test_blog(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title="Title 1", body="response body")
        Article.objects.create(title="Title 2", body="response body")
        self.assertEqual(len(Article.objects.all()), 2)

        a = Article.objects.get(pk=2)
        self.assertEqual(a.title, "Title 2")

        a.title = "New title"
        a.save()
        self.assertEqual(a.title, "New title")

        a.delete()
        self.assertEqual(len(Article.objects.all()), 1)
