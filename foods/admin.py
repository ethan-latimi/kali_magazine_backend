from django.contrib import admin
from .models import FoodCategory, FoodPost

# Food Admin Register

admin.site.register(FoodCategory)
admin.site.register(FoodPost)