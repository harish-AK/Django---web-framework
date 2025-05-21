from django.db import models



# Menu category
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_category_name

# Menu
class Menu(models.Model):
    dish_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    hotel = models.CharField(max_length=100)
    category_id = models.ForeignKey(MenuCategory,on_delete=models.PROTECT,null=True,blank=True)

    def __str__(self):
        return f"{self.dish_name} {self.cuisine} {self.price} {self.hotel}"

