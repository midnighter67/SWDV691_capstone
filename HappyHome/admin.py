from django.contrib import admin
from .models import Provider, User, Category, Classification, Review, Reply

# models
admin.site.register(Provider)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Classification)
admin.site.register(Review)
admin.site.register(Reply)