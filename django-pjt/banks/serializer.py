from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, FilteringOptions, FilteringSavingOptions

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class FilterOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteringOptions
        fields = '__all__'

class FilterSavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteringSavingOptions
        fields = '__all__'

class DepositProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class SavingProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
