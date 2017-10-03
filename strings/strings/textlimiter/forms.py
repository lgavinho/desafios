from django import forms


class TextForm(forms.Form):
    source = forms.CharField(label='Source Text', widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    line_size = forms.IntegerField(label='Line Size (chars)', required=True, initial=40)
    justify = forms.BooleanField(label='Justify', required=False)