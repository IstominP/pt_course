from django.db import models

# Create your models here.


class Foo(models.Model):
	name = models.CharField(max_length=30)


class FooBar(models.Model):
	name = models.CharField(max_length=30)


class FooBarFoo(models.Model):
	name = models.CharField(max_length=30)