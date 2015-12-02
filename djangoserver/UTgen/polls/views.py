from django.shortcuts import render
# from django.http import HttpResponse

from .forms import *


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = viite_vorm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/vastus/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = viite_vorm()

    return render(request, 'vorm.html', {'form': form})

# Create your views here.
