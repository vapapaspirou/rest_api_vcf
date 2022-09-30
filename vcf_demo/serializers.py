from rest_framework import serializers

from vcf_demo.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        username = serializers.HiddenField(default=serializers.CurrentUserDefault())
        fields = '__all__'
