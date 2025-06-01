from django import forms

SHIFT = (
    ('1','batman'),
    ('2','superman'),
    ('3','wonderwoman'),

)


class DemoForm(forms.Form):
    name = forms.CharField()
    shift = forms.ChoiceField(choices=SHIFT)
    time = forms.TimeField()
