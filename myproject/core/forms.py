from django import forms


class EmailForm(forms.Form):
    email_to = forms.EmailField(label='To')
    title = forms.CharField(max_length=140)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ('email_to', 'title', 'message')
