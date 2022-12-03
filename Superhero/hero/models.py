from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


def get_upload(instance, filename):
    return f"images/{filename}"

class Photo (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

class Investigator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy("investigator_detail", args=[str(self.id)])

    @property
    def articles(self):
        return Article.objects.filter(investigator=self)

    @property
    def name(self):
        return self.user.first_name + " " + self.user.last_name

    @staticmethod
    def get_me(user):
        return Investigator.objects.get_or_create(user=user)[0]


class Superhero(models.Model):
    investigator = models.ForeignKey(
        Investigator, on_delete=models.CASCADE, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.CharField(max_length=100)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True)
    strengths = models.CharField(max_length=100)
    weaknesses = models.CharField(max_length=100)

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy("hero_list")


class Article(models.Model):
    investigator = models.ForeignKey(
        Investigator,
        on_delete=models.CASCADE,
        editable=False,
        related_name="messages_sent",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    superheroes = models.ManyToManyField(Superhero)
    title = models.CharField(max_length=100)
    text = models.TextField()

    @property
    def articles(self):
        return Article.objects.filter(Investigator=self.investigator)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy("article_detail", args=[str(self.id)])

