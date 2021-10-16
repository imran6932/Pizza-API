from django.contrib import admin
from pizza_api.models import Pizza

# Register your models here.

@admin.register(Pizza)
class PizaaAdmin(admin.ModelAdmin):
    """
    Pizza Admin class created for display all pizza instances 
    in Admin panel.
    
    """
    list_display = ['id', 'pizza_type', 'pizza_size', 'toppings']
