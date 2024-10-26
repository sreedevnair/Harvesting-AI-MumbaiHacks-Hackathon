from django import forms

class FarmingForm(forms.Form):
    crop = forms.CharField(label="Crop Type", max_length=100)
    soil_type = forms.CharField(label="Soil Type", max_length=100)
    location = forms.CharField(label="Location", max_length=100)
