from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category_Type(models.Model):
    title = models.CharField(max_length=200, blank=True)
    type = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )

    def __str__(self):
        return self.title


class Category_Meals(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category_LowCarb(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ProductData(models.Model):
    Flavor = models.CharField(max_length=10000, blank=True)
    company = models.CharField(max_length=10000, blank=True)
    formation = models.CharField(max_length=10000, blank=True)
    origin = models.CharField(max_length=10000, blank=True)
    serving = models.CharField(max_length=10000, blank=True)
    weight = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.Flavor


class Meal(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=200, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    cooking = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(
        Category_Meals, on_delete=models.CASCADE, related_name="category"
    )

    def __str__(self):
        return self.title


class TopProducts(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=10000, blank=True)
    image = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    price = models.FloatField()
    nutrition = models.CharField(max_length=200, blank=True)
    ingredient = models.CharField(max_length=200, blank=True)
    cooking = models.CharField(max_length=200, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField()
    sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TopArrival(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    brandUrl = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200)
    nutrition = models.CharField(max_length=100, blank=True)
    cooking = models.CharField(max_length=100, blank=True)
    ingredient = models.CharField(max_length=200, blank=True)
    body = models.CharField(max_length=10000, blank=True)
    weight = models.CharField(max_length=200, blank=True)
    amount = models.IntegerField()
    sale = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Chicken(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    calories = models.FloatField()
    image = models.CharField(max_length=200)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Snack(models.Model):
    amount = models.IntegerField()
    brand = models.CharField(max_length=10000, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    image = models.CharField(max_length=200)
    piece = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Supplements(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    calories = models.FloatField()
    image = models.CharField(max_length=200)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Fruit(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    calories = models.FloatField()
    image = models.CharField(max_length=200)
    piece = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Keto(models.Model):
    amount = models.IntegerField()
    brand = models.CharField(max_length=10000, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    image = models.CharField(max_length=200)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title


class Vegetables(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    calories = models.FloatField()
    image = models.CharField(max_length=200)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class BreakFast_Meals(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    category = models.CharField(max_length=200, blank=True)
    cooking = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Lunch_Meal(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    category = models.CharField(max_length=200, blank=True)
    cooking = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class LowCarb(models.Model):
    amount = models.IntegerField(blank=True)
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=10000, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField(blank=True)
    category = models.ForeignKey(
        Category_LowCarb,
        on_delete=models.CASCADE,
        related_name="category_lowcarb",
    )
    image = models.CharField(max_length=200, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField(blank=True)
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=200, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    cooking = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=200, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    weight = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(
        Category_Type, on_delete=models.CASCADE, related_name="category1"
    )
    type = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="type")

    def __str__(self):
        return self.title


class Bakeries(models.Model):
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    category = models.CharField(max_length=2000, blank=True)
    contain = models.CharField(max_length=2000, blank=True)
    image = models.CharField(max_length=2000)
    ingredient = models.CharField(max_length=2000, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    storing = models.CharField(max_length=2000, blank=True)
    title = models.CharField(max_length=10000, blank=True)
    weight = models.CharField(max_length=2000, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Vegan(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=200, blank=True)
    brandUrl = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    category = models.CharField(max_length=2000, blank=True)
    image = models.CharField(max_length=2000)
    ingredient = models.CharField(max_length=2000, blank=True)
    nutrition = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=10000, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Meat(models.Model):
    amount = models.IntegerField()
    body = models.CharField(max_length=10000, blank=True)
    brand = models.CharField(max_length=200, blank=True)
    calories = models.FloatField()
    category = models.CharField(max_length=2000, blank=True)
    image = models.CharField(max_length=2000)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    title = models.CharField(max_length=10000, blank=True)
    weight = models.CharField(max_length=2000, blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Register(models.Model):
    username = models.CharField(max_length=10000, blank=True)
    email = models.CharField(max_length=10000, blank=True)
    password = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username


class AddedMeal(models.Model):
    title = models.CharField(max_length=10000, blank=True)
    body = models.CharField(max_length=10000, blank=True)
    image = models.CharField(max_length=2000,blank=True)
    price = models.FloatField(blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


class AddNewMeal(models.Model):
    title = models.CharField(max_length=10000, blank=True)
    body = models.CharField(max_length=10000, blank=True)
    image = models.CharField(max_length=2000,blank=True)
    price = models.FloatField(blank=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title


