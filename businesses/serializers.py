from rest_framework import serializers
from .models import BusinessCategory, BusinessPost


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = '__all__'

class BusinessPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPost
        fields = '__all__'
