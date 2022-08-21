from django.contrib import admin

# Register your models here.
from .models import (
    AddNewMeal,
    AddedMeal,
    Category,
    Category_LowCarb,
    Category_Meals,
    Chicken,
    Fruit,
    Keto,
    LowCarb,
    Meal,
    Snack,
    Supplements,
    TopArrival,
    TopProducts,
    Vegetables,
    Register,
)

admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(TopArrival)
admin.site.register(TopProducts)
admin.site.register(Chicken)
admin.site.register(Snack)
admin.site.register(Supplements)
admin.site.register(Fruit)
admin.site.register(Keto)
admin.site.register(Vegetables)
admin.site.register(Category_Meals)
admin.site.register(Category_LowCarb)
admin.site.register(LowCarb)
admin.site.register(Register)
admin.site.register(AddedMeal)
admin.site.register(AddNewMeal)
