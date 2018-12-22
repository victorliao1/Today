from django import forms

class addTodo_form(forms.Form):
    topic = forms.CharField(label = 'Topic', required = True)
