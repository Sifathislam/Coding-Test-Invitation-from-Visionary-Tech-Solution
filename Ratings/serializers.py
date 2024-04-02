from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


# ====================  This Model is created for User Registation  =============================  #
class RegistrationSerializer(serializers.ModelSerializer):
    # ============= For Account Details and confirm password  ================ #
    confirm_password = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(max_length=13,write_only=True, required=True)
    name = serializers.CharField(max_length=200,write_only=True, required=True)

    # ============= Fields will Show in API  ================ #
    class Meta:
        model = User
        fields = ['username','name','email', 'phone', 'password', 'confirm_password']

    # ============= Check The password and Email  =============== #
    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    # ========= Create Account and Deactivate the account   ============= #
    def create(self, validated_data):
    # ==== Store 'name' and 'phone' values before removing them from validated_data =====
        name = validated_data.pop('name')
        phone = validated_data.pop('phone')

        # ==== Delete data not need to create user === # 
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data, is_active=False) 


    # ========= Create account model ============= #  
        models.account_Model.objects.create(user=user, name=name, phone=phone,email=validated_data['email'])
        return user

# ==============================   Account Login Serializer   ============================== #
class userLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


# ========================== View All User Serializer   ============================= #
class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# ============================= Create Movie Serializer   ============================= #
class MovieSerializer(serializers.ModelSerializer):
    # ==== Add method field for show the avrage ratings ===#
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = models.movie_Model
        fields = ['id', 'name', 'genre', 'rating', 'release_date', 'average_rating']

    # ==== get avrage ratings ===#
    def get_average_rating(self, obj):
        return obj.average_rating()


# ============================= Create Movie Serializer   ============================= #
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rating_Model
        fields = '__all__'