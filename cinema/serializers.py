from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=1000)
    duration = serializers.IntegerField()
    
    class Meta:
        model = Movie
        fields = ["id", "description", "duration"]

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
