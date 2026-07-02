from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):

    def validate_release_year(self, value):
        if value < 1975:
            raise serializers.ValidationError("Release year cannot be before 1975.")
        
        return value
    
    def validate_global_sales(self, value):
        if value < 0:
            raise serializers.ValidationError("Global sales cannot be a negative value.")
        
        return value

    class Meta:
        model = Game
        fields = [
        'id',
        'name',
        'platform',
        'genre',
        'publisher',
        'release_year',
        'na_sales',
        'eu_sales',
        'jp_sales',
        'other_sales',
        'global_sales'
        ]