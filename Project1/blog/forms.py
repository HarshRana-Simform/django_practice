from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from blog.models import Posts_db

# Created through form API
# class add_post(forms.Form):
#     # Built-in validators
#     title = forms.CharField(
#         validators=[
#             validators.MaxLengthValidator(100),
#         ])
#     author = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea(
#         attrs={'placeholder': 'Enter a description'}))

#     # Field specific validation
#     def clean_title(self):
#         title_value = self.cleaned_data['title']

#         if len(title_value) < 3:
#             raise forms.ValidationError(
#                 'Enter more than or equal to 3 charaters.')
#         return title_value

# All fields validate at together
# def clean(self):
#     cleaned_data = super().clean()
#     title_value = cleaned_data.get('title')
#     author_value = cleaned_data.get('author')

#     if title_value and len(title_value) < 3:
#         self.add_error('title', 'Enter more than or equal to 3 charaters.')

#     return cleaned_data

# Created through model form


class add_post(forms.ModelForm):
    class Meta:
        model = Posts_db
        fields = ['title', 'author', 'content', 'banner']
        widget = {
            'content': forms.Textarea(attrs={'placeholder': 'Enter a description'})
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
