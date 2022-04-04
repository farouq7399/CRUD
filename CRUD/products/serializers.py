from rest_framework import serializers
from .models import product
from django.contrib.auth.models import User



class productSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    slug = serializers.SlugField()

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        return product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('title', instance.title)
        instance.save()
        return instance
