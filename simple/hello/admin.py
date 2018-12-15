from django.contrib import admin
from models import Foo, FooBar, FooBarFoo

# Register your models here.
admin.site.register(Foo)
admin.site.register(FooBar)
admin.site.register(FooBarFoo)