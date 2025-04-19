from .models import Test, Baza
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class TestSolveForm(forms.Form):
    def __init__(self, *args, tests=None, **kwargs):
        super().__init__(*args, **kwargs)
        if tests:
            for test in tests:
                options = []
                for variant in ['a', 'b', 'c', 'd']:
                    text = getattr(test, variant)
                    if text:
                        options.append((variant, f"{variant.upper()}) {text}"))
                self.fields[f'test_{test.id}'] = forms.ChoiceField(
                    label=test.savol,
                    choices=options,
                    widget=forms.RadioSelect,
                    required=True
                )


class BazaForm(forms.ModelForm):
    class Meta:
        model = Baza
        fields = ['name']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['last_name', 'image', 'password1', 'password2']


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['savol', 'image', 'a', 'b', 'c', 'd', 'true_var', 'times']
