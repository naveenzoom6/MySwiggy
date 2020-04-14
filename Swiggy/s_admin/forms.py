
from django import forms
from s_admin.models import StateModel
from s_admin.models import CityModel
from s_admin.models import AreaModel

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('state_name',)

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"
        exclude = ('city_no',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = "__all__"
        exclude = ('area_no',)