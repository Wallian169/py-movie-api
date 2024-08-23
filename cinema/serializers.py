from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=1000)
    duration = serializers.IntegerField()

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
