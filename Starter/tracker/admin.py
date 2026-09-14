from django.contrib import admin
from tracker.models import Category, Transactions

# Register your models here.
admin.site.register(Transactions)
admin.site.register(Category)
