from django import forms
from .models import RecipeModels
from django import forms
from django.contrib.auth.models import User


from django import forms
from .models import RecipeModels


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModels
        fields = ['title', 'description', 'image', 'category']

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            self.add_error('password2', 'As senhas não coincidem')

        return cleaned_data