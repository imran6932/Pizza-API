from rest_framework import serializers
from pizza_api.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    """
    PizzaSerializer class created to serialize model class.

    """
    class Meta:
        model = Pizza
        fields = ['pizza_type', 'pizza_size', 'toppings']

    def validate_pizza_type(self, value):
        """
        validation error added for field pizza_type.
        the value only takes Regular and Square pizza types.
        
        """
        if value.lower() not in ('regular', 'square'):
            raise serializers.ValidationError('Pizza type must be Regular or Square')
        return value

    def validate_pizza_size(self, value):
        """
        validation error added for field pizza_size.
        it takes only sizes which is defined here.
        
        """
        if value.lower() not in ('small', 'medium', 'large', 'extra large'):
            raise serializers.ValidationError('Sorry  given size is not available')
        return value

    def validate_toppings(self, value):
        """
        validation for toppings value only be string value.
        
        """
        val = type(value)
        print(val)
        if not value.isalpha():
            raise serializers.ValidationError('value must be string')
        return value



        
    