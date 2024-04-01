from rest_framework import serializers
from .models import FoodCategory, FoodPost


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'

class FoodPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPost
        fields = '__all__'
