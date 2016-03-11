from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    created_date = models.DateTimeField(auto_now=True)
    visible_from_date = models.DateTimeField()
    visible_till_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def is_visible(self):
        current_time = timezone.now()
        return current_time > self.visible_from_date and current_time < self.visible_till_date

class Banner(models.Model):
    img = models.ImageField(upload_to='static/images/banners')
    is_active = models.BooleanField()


class SiteTextData(models.Model):
    unique_identifier = models.CharField(max_length=20)
    data = models.TextField()

    def __str__(self):
        return self.unique_identifier


class PeopleType(models.Model):
    name = models.CharField(max_length=40)
    display_text = models.CharField(max_length=40)
    order = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class People(models.Model):
    list_on = models.ForeignKey(PeopleType)
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=100, blank=True)
    interest = models.TextField()
    url = models.CharField(max_length=20, blank=True)
    personal_page = models.BooleanField(default=False)
    short_bio = models.TextField(blank=True)
    study_one_line = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    homepage = models.CharField(max_length=100, blank=True)
    login = models.OneToOneField(User)
    img = models.ImageField(upload_to='static/images/people')

    def __str__(self):
        return self.name

    def http_link(self):
        return '/personal/' + self.url


class ShortNames(models.Model):
    name = models.CharField(max_length=30)
    profile = models.ForeignKey(People, blank=True)

    def __str__(self):
        return self.name

    def display(self):
        if self.profile is None:
            return self.__str__()
        else:
            return '<a href="/personal/' + self.profile.url + '">' + self.__str__() + '</a>'

class ConferenceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Publication(models.Model):
    author = models.ManyToManyField(ShortNames)
    conf_type = models.ForeignKey(ConferenceType)
    published_at = models.CharField(max_length=200)
    published_page = models.CharField(max_length=20)
    published_year = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def authors(self):
        authors = self.author.all()
        list = []
        for author in authors:
            list.append(author.display())
        return ','.join(list)



