from rest_framework import serializers

from car_app.models import Brand, Car


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        # fields = ('title')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        brand = BrandSerializer(Brand.objects.get(brand=instance.id)).data
        print(brand)
        representation['brand'] = brand
        return representation