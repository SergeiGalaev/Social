from django import forms



class student(forms.Form):
    student = forms.CharField(label='Student', max_length=1000000)
