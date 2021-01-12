from django import forms

class UserForm(forms.Form):
    quote_text = forms.CharField(label="цитата", required=False)
    question_text = forms.CharField(label="Ваш вопрос", widget=forms.Textarea)
    
    
