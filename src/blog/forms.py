from django import forms    #ModelForm, TextInput, Textarea, Select
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','content','image','tag')
       
        	# 'content' : Textarea(atrrs={'class':'form-control','rows':4}),
        	# 'tag' : Select(atrrs={'class':'form-control'}),

