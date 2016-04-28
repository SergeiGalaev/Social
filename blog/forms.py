from django import forms

class NameForm(forms.Form):
    post = forms.CharField(label='Your post', max_length=10000)


class student(forms.Form):
    student = forms.CharField(label='Student', max_length=1000000)