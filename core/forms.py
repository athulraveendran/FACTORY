from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Banglore, Mumbai, Chennai
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_branch')



class BangloreForm(ModelForm):
    class Meta:
        model=Banglore
        fields='__all__'
        widgets={
            'date':forms.DateInput(attrs=dict(type='date')),
            'line1':forms.TextInput(attrs={'class':'form-control'}),
            'line2':forms.TextInput(attrs={'class':'form-control'}),
            'line3':forms.TextInput(attrs={'class':'form-control'}),
            'line4':forms.TextInput(attrs={'class':'form-control'}),
            'line5':forms.TextInput(attrs={'class':'form-control'})
        }

class MumbaiForm(ModelForm):
    class Meta:
        model=Mumbai
        fields='__all__'
        widgets={
            'date':forms.DateInput(attrs=dict(type='date')),
            'line1':forms.TextInput(attrs={'class':'form-control'}),
            'line2':forms.TextInput(attrs={'class':'form-control'}),
            'line3':forms.TextInput(attrs={'class':'form-control'}),
        }

class ChennaiForm(ModelForm):
    class Meta:
        model=Chennai
        fields='__all__'
        widgets={
            'date':forms.DateInput(attrs=dict(type='date')),
            'line1':forms.TextInput(attrs={'class':'form-control'}),
            'line2':forms.TextInput(attrs={'class':'form-control'}),
            'line3':forms.TextInput(attrs={'class':'form-control'}),
            'line4':forms.TextInput(attrs={'class':'form-control'}),
            'line5':forms.TextInput(attrs={'class':'form-control'})
        }

