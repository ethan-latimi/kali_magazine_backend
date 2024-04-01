from rest_framework import serializers
from .models import LifestyleCategory, LifestylePost


class LifestyleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LifestyleCategory
        fields = '__all__'

class LifestylePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifestylePost
        fields = '__all__'
