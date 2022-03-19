from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Comment





class SingUpForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2','gender']

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Emails is already taken")
            return email
        

class CommentForm(forms.ModelForm):
    comment=forms.CharField(max_length=200, 
                    widget=forms.TextInput(attrs={'placeholder': 'Add Comment'}))
    class Meta:
        model=Comment
        fields=['comment']
        placeholder={
            'comment':'Add Comment'
        }