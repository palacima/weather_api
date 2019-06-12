from django.forms import ModelForm, TextInput
from .models import Weather

class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['lat', 'long', 'source']
        widgets = {
            'lat': FloatInput(attrs={'class' : 'input', 'placeholder' : 'Latitude'}),
            'long': FloatInput(attrs={'class' : 'input', 'placeholder' : 'Longitude'}),
            'source': TextInput(attrs={'class' : 'input', 'placeholder' : 'Source(s)'}),
        }
