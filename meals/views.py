from unicodedata import category
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, UpdateAPIView
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
    TopProducts,
    TopArrival,
    Vegetables,
    Products,
    Category_Type,
    Register,
    Vegan,
    Meat
)
from .serializers import (
    AddNewMealSerializer,
    AddedMealSerializer,
    BreakFast_MealSerializer,
    Category_LowCarbSerializer,
    Category_MealsSerializer,
    CategorySerializer,
    ChickenSerializer,
    FruitSerializer,
    KetoSerializer,
    LowCarbSerializer,
    Lunch_MealSerializer,
    MealSerializer,
    SnackSerializer,
    SupplementsSerializer,
    TopProductsSerializer,
    TopArrivalSerializer,
    VegetablesSerializer,
    ProductsSerializer,
    Category_TypeSerializer,
    RegisterSerializer,
    UserSerializer,
    BakeriesSerializer,
    VeganSerializer,
    MeatSerializer,
)

from rest_framework import viewsets, generics
from rest_framework import permissions


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def mealAPI(request, meal_id=0):
    if request.method == "GET":
        if meal_id == 0:
            meals = Meal.objects.all()
            return JsonResponse(MealSerializer(meals, many=True).data, safe=False)
        else:
            try:
                meals = Meal.objects.get(pk=meal_id)
                return JsonResponse(MealSerializer(meals).data, safe=False)
            except Meal.DoesNotExist:
                return HttpResponse("Meal not found", status=404)

    elif request.method == "DELETE":
        try:
            Meal.objects.get(pk=meal_id).delete()
            return HttpResponse("Meal deleted successfully", status=204)
        except Meal.DoesNotExist:
            return HttpResponse("Meal not found", status=404)

    else:
        return HttpResponse("Method not allowed")


class MealList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Meal.objects.all()

    serializer_class = MealSerializer


class MealDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Meal.objects.all()

    serializer_class = MealSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category.objects.all()

    serializer_class = CategorySerializer


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Category.objects.all()

    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class TopProductsList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = TopProducts.objects.all()

    serializer_class = TopProductsSerializer


class TopProductsDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = TopProducts.objects.all()

    serializer_class = TopProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TopArrivalList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = TopArrival.objects.all()

    serializer_class = TopArrivalSerializer


class TopArrivalDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = TopArrival.objects.all()

    serializer_class = TopArrivalSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ChickenList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Chicken.objects.all()

    serializer_class = ChickenSerializer


class ChickenDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Chicken.objects.all()

    serializer_class = ChickenSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SnackList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Snack.objects.all()

    serializer_class = SnackSerializer


class SnackDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Snack.objects.all()

    serializer_class = SnackSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SupplementsList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Supplements.objects.all()

    serializer_class = SupplementsSerializer


class SupplementsDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Supplements.objects.all()

    serializer_class = SupplementsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FruitList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Fruit.objects.all()

    serializer_class = FruitSerializer


class FruitDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Fruit.objects.all()

    serializer_class = FruitSerializer
    # permission_classes = [permissions.IsAuthenticated]


class KetoList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Keto.objects.all()

    serializer_class = KetoSerializer


class KetoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Keto.objects.all()

    serializer_class = KetoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class VegetablesList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Vegetables.objects.all()

    serializer_class = VegetablesSerializer


class VegetablesDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Vegetables.objects.all()

    serializer_class = VegetablesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BreakFast_MealList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = BreakFast_Meals.objects.all()

    serializer_class = BreakFast_MealSerializer


class BreakFast_MealDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = BreakFast_Meals.objects.all()

    serializer_class = BreakFast_MealSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Lunch_MealList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Lunch_Meal.objects.all()

    serializer_class = Lunch_MealSerializer


class Lunch_MealDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Lunch_Meal.objects.all()

    serializer_class = Lunch_MealSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Category_MealsList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category_Meals.objects.all()

    serializer_class = Category_MealsSerializer


class Category_MealsDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Category_Meals.objects.all()

    serializer_class = Category_MealsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Category_LowCarbList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category_LowCarb.objects.all()

    serializer_class = Category_LowCarbSerializer


class Category_LowCarbDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Category_LowCarb.objects.all()

    serializer_class = Category_LowCarbSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LowCarbList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = LowCarb.objects.all()

    serializer_class = LowCarbSerializer


class LowCarbDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = LowCarb.objects.all()

    serializer_class = LowCarbSerializer
    # permission_classes = [permissions.IsAuthenticated]
class MeatList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Meat.objects.all()

    serializer_class = MeatSerializer


class MeatDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Meat.objects.all()

    serializer_class = MeatSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ProductsList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Products.objects.all()
    # queryset=Products.objects.filter(type=Category_Type.type)
    

    serializer_class = ProductsSerializer


class ProductsDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Products.objects.all()
    # queryset=Products.objects.filter(type=Category_Type.type)
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
    
    # def get_queryset(self):
    #     user_id = self.kwargs['user_id']
    #     user = User.objects.get(pk=user_id)
    #     return Products.objects.filter(type=Category_Type.type)

class Category_TypeList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category_Type.objects.all()

    serializer_class = Category_TypeSerializer
    


class Category_TypeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Category_Type.objects.all()

    serializer_class = Category_TypeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
class RegisterList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Register.objects.all()

    serializer_class = RegisterSerializer
    


class RegisterDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Register.objects.all()

    serializer_class = RegisterSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
 
class BakeriesList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Bakeries.objects.all()

    serializer_class = BakeriesSerializer
    


class BakeriesDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Bakeries.objects.all()

    serializer_class = BakeriesSerializer
    # permission_classes = [permissions.IsAuthenticated]
 
class VeganList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Vegan.objects.all()

    serializer_class = VeganSerializer
    


class VeganDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = Vegan.objects.all()

    serializer_class = VeganSerializer
    # perm      
class AddedMealList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = AddedMeal.objects.all()

    serializer_class = AddedMealSerializer
    


class AddedMealDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = AddedMeal.objects.all()

    serializer_class = AddedMealSerializer
    # perm      
class AddNewMealList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = AddNewMeal.objects.all()

    serializer_class = AddNewMealSerializer
    


class AddNewMealDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    lookup_field = "id"

    queryset = AddNewMeal.objects.all()

    serializer_class = AddNewMealSerializer
    # perm      
class SignUp(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


