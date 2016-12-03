from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile

class CategoryForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Please enter a category name")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
  likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
  slug = forms.CharField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Category
    # tuple specifying the classes we want to use
    fields = ('name', )

class PageForm(forms.ModelForm):
  title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
  url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

  class Meta:
    model = Page
    # excluding the category foreign key field from the form
    exclude = ('category', 'slug')

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter your password")

  class Meta:
    model = User
    fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('website', 'picture') 
