from django.contrib import admin
from .models import FoodType, Food, Comment

class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    search_fields = ('name',) 
    list_filter = ('name',) 

class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'food_type', 'price') 
    search_fields = ('name', 'food_type__name') 
    list_filter = ('food_type', 'price')  
    list_editable = ('price',) 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'author', 'created')  
    search_fields = ('food__name', 'author__username')  
    list_filter = ('created',)  

admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment, CommentAdmin)
