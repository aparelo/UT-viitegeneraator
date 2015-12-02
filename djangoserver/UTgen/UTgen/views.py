from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import datetime
from .forms import NameForm
# from backend import generate_viide

def generate_viide(Title, date, tuup, source='', author='', link='', version='', page_start='', page_end=''):
    # Vorgumaterjal
    if tuup == "Võrgumaterjal":
        viide = Title + ", " + source + '. [' + tuup + '] [Tsiteeritud: ' + date + '] ' + link
        return viide
    elif tuup == 'PDF':
        viide = Title + ", " + source + '. [' + tuup + '] [Laetud alla: ' + date + '] ' + link
        return viide
    elif tuup == 'raamat':
        viide = author + ', ' + title, + ', ' + version + ', ' + source
        return viide
    elif tuup == 'artikkel':
        # hetkel ainult uks autor
        viide = author + ', ' + title + ', ' + source, + ', lk ' + page_start + '-' + page_end + ', ' + date
        return viide
    else:
        return False


def proov(sisend):
    return sisend + 6


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/vastus/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'vorm.html', {'form': form})


def current_datetime(request):
    now = proov(5)
    html = "<h1>Kell on praegu %s</h1>" %now
    return HttpResponse(html)
