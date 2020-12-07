from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'type_of_food', 'affordability', 'phone', 'website', 'dine_in',
                  'take_out', 'google_maps_code', 'image']
