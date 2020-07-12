from django.forms import ModelForm
from .models import Widget

class WidgetNewForm(ModelForm):
  class Meta:
    model = Widget
    fields = ['description', 'quantity']