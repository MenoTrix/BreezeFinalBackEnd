from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate



from .models import (
    AddNewMeal,
    AddedMeal,
    Bakeries,
    BreakFast_Meals,
    Category,
    Category_LowCarb,
    Category_Meals,
    Chicken,
    Fruit,
    Keto,
    LowCarb,
    Lunch_Meal,
    Meal,
    Snack,
    Supplements,
    TopArrival,
    TopProducts,
    Vegetables,
    Products,
    Category_Type,
    Register,
    Vegan,
    Meat
)

UserModel = get_user_model()
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TopProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProducts
        fields = "__all__"


class TopArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopArrival
        fields = "__all__"


class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = "__all__"


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = "__all__"


class SupplementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplements
        fields = "__all__"


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = "__all__"


class KetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keto
        fields = "__all__"


class VegetablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetables
        fields = "__all__"


class BreakFast_MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakFast_Meals
        fields = "__all__"


class Lunch_MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lunch_Meal
        fields = "__all__"


class Category_MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Meals
        fields = "__all__"


class Category_LowCarbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_LowCarb
        fields = "__all__"


class LowCarbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowCarb
        fields = "__all__"
class BakeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bakeries
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class Category_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Type
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"
        
class VeganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = "__all__"
        
class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = "__all__"
class AddedMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddedMeal
        fields = "__all__"
class AddNewMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddNewMeal
        fields = "__all__"
        
        
        
        
class UserSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            # is_staff=validated_data['is_staff']
        )
        return user

    def update(self, validated_data):

        user = UserModel.objects.update_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("username", "password", "email")

