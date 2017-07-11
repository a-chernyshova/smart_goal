from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    value = models.IntegerField(unique=True)
    name = models.CharField(verbose_name='priority', max_length=32, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    value = models.IntegerField()
    name = models.CharField(verbose_name='status', max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='category', max_length=120, unique=True)
    image = models.ImageField(default='media/default.jpg', blank=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField(verbose_name='title', max_length=120, blank=False)
    author = models.ForeignKey(User)
    description = models.TextField(verbose_name='description', blank=False)
    created_date = models.DateTimeField(verbose_name='Date of creation')
    priority = models.ForeignKey(Priority)
    img = models.ImageField(default='media/default.jpg', blank=True)
    attachments = models.FileField(blank=True)
    status = models.ForeignKey(Status)
    category = models.ForeignKey(Category)
    deadline = models.DateField(blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField(max_length=320, blank=False)
    task = models.ForeignKey(Tasks)

    def __str__(self):
        return self.body


class Sub_tasks(models.Model):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Tasks)
    title = models.CharField(verbose_name='title', max_length=120, blank=False)
    description = models.TextField()
    status = models.ForeignKey(Status)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title
