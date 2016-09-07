from django import forms    #ModelForm, TextInput, Textarea, Select
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','content','tag')
       
        	# 'content' : Textarea(atrrs={'class':'form-control','rows':4}),
        	# 'tag' : Select(atrrs={'class':'form-control'}),

# from django.forms import ModelForm, Textarea
# from myapp.models import Author

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }