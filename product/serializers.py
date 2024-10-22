from rest_framework import serializers
from .models import Product
from .models import ProductsImage
from urllib.parse import urlparse

class ProductsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    images =  ProductsImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(allow_empty_file=False, use_url=False),write_only=True,  required=False)
    removed_images = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)

    class Meta:
        model = Product
        fields = ["id", "title", "description", "price",  "images", "uploaded_images", "removed_images"]
    
    def create(self, validated_data):
        if "uploaded_images" in validated_data:
            uploaded_images = validated_data.pop("uploaded_images")
            product = Product.objects.create(**validated_data)
            for image in uploaded_images:
                ProductsImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        if "uploaded_images" in validated_data:
            uploaded_images = validated_data.pop("uploaded_images")
            for image in uploaded_images:
                ProductsImage.objects.create(product=instance, image=image)

        if "removed_images" in validated_data:
            removed_images = validated_data.pop("removed_images")
            for image in removed_images:
                parsed_url = urlparse(image)
                image_path = parsed_url.path.replace("/media/", "")
                obj = ProductsImage.objects.filter(product=instance, image=image_path)
                if obj:
                    obj.delete()
        return instance