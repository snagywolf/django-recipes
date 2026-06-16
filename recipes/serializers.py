from rest_framework import serializers
from .models import RecipeModels

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModels

        fields = '__all__'

        read_only_fields = [
            'author',
            'is_published',
            'created_at',
            'updated_at',
        ]