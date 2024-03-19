from rest_framework import serializers

from . import models


class drinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Drink
        fields=["id","name","decription"]