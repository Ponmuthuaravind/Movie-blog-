from django import forms
from .models import MovieModel,CommentsModel

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'
        widgets = {'relesed_on':forms.DateInput(attrs={'type':'date'}),
                   'reviewed_on':forms.DateInput(attrs={'type':'date'})}
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = '__all__'