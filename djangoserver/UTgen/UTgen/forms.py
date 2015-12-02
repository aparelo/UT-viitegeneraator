from django import forms


class NameForm(forms.Form):
    pealkiri = forms.CharField(label='pealkiri')
    # radio = forms.BooleanField(label='boolean')
    # date = forms.DateField(label='date')
    # drop_down = forms.ChoiceField(choices=['uks', 'kaks', 'kolm'], label='drop_down')
