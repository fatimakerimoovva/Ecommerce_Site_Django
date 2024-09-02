from rest_framework import serializers
from product.models import Product, ProductVersion, Category, Manufacturer, Color, Images

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = [
            'id',
            'image',
            'title',
        ]
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'id',
            'name',
            'image',
        ]

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'id',
            'name',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]

class ProductReadSerializers(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'old_price',
            'price',
            'in_sale',
            'manufacturer',
            'new',
            
        ]

class ProductVersionSerializer(serializers.ModelSerializer):
    image = ImagesSerializer(many=True)
    product = ProductReadSerializers()
    color = ColorSerializer()
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductVersion
        fields = [
            'id',
            'product',
            'cover_image',
            'color',
            'image',
            'detail_url',
            'quantity',
        ]
        
    def get_detail_url(self, obj):
        return obj.get_absolute_url()


    
    
class ProductsSerializer(serializers.ModelSerializer):
    product_version = ProductVersionSerializer(many=True)
    category = CategorySerializer()
    manufacturer = ManufacturerSerializer()
    total_quantity = serializers.SerializerMethodField()
    detail_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'old_price',
            'in_sale',
            'price',
            'product_version',
            'category',
            'manufacturer',
            'total_quantity',
            'detail_url',
            'new',
            
        ]
        
    def get_detail_url(self, obj):
        return obj.get_absolute_url()

    def get_total_quantity(self, obj):
        return obj.total_quantity
    
    def get_version(self, obj):
        return ProductVersionSerializer(many=True).data