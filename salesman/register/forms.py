from django import forms
from models import User

class FormUser(forms.ModelForm):
   class Meta:
      model = User




