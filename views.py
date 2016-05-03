from django.shortcuts import render, get_object_or_404

from .models import	Student
from .models import	Parents
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import NameForm


def	post_list(request):
	students = Student.objects.all()
	return render(request, 'blog/post_list.html', {'student': students})

def	post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return	render(request,	'blog/post_detail.html', {'student': students})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = student(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = student()

    return render(request, 'name.html', {'form': form})
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

