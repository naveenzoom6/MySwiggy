
from django import forms
from restaurant.models import RestaurantModel

class RestaurantForm(forms.ModelForm):
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = RestaurantModel
        fields = "__all__"
        exclude = ('restro_id','restro_otp','restro_status')