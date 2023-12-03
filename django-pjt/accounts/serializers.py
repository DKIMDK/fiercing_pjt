from banks.serializer import DepositProductOptionSerializer, DepositProductSerializer, SavingProductSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    # 나머지 필드들은 RegisterSerializer 에 있음
    # 회원가입 시 추가로 필요한 필드들을 모두 정의.
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    age = serializers.IntegerField(required=False)
    asset = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'asset': self.validated_data.get('asset', ''),
            'salary': self.validated_data.get('salary', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        # if "password1" in self.cleaned_data:
        #     try:
        #         adapter.clean_password(self.cleaned_data['password1'], user=user)
        #     except DjangoValidationError as exc:
        #         raise serializers.ValidationError(
        #             detail=serializers.as_serializer_error(exc)
        #         )
        user.save()
        self.custom_signup(request, user)
        # setup_user_email(request, user, [])
        return user
    

class CustomUserDetailsSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    age = serializers.IntegerField(required=False)
    asset = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'age', 'nickname', 'salary', 'asset', 'deposit_products', 'saving_products')

    def get_cleaned_data(self):
        return {
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'asset': self.validated_data.get('asset', ''),
            'salary': self.validated_data.get('salary', ''),
        }
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        # instance.username = validated_data.get('username', None)
        instance.age = validated_data.get('age', None)
        instance.nickname = validated_data.get('nickname', None)
        instance.salary = validated_data.get('salary', None)
        instance.asset = validated_data.get('asset', None)
        instance.save()
        return instance
    
    def save(self):
        # self.validated_data.pop('username', None)
        user = super().save()
        user.age = self.validated_data.get('age', None)
        user.nickname = self.validated_data.get('nickname', None)
        user.salary = self.validated_data.get('salary', None)
        user.asset = self.validated_data.get('asset', None)
        user.save()
        return user
    
class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'age', 'asset', 'salary', 'saving_products', 'deposit_products')

class SavingSerializer(serializers.ModelSerializer):
    saving_products = SavingProductSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__' 

class DepositSerializer(serializers.ModelSerializer):
    deposit_products = DepositProductSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'