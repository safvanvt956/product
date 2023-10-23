from django.contrib import admin
from .models import Category, Subcategory, Product 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slue' ,'image','parshapa')  
    prepopulated_fields = {'slue': ('title',)} 


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slue','parshapa','image', 'category')  # Corrected to 'slue' instead of 'slug'
    prepopulated_fields = {'slue': ('title',)}  # Use 'slue' instead of 'slug'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','image','oldprice','subcategory')  # Removed 'image' from list_display

    




    
