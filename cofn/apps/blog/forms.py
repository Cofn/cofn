from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=80)
    body_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}))

    class Meta:
        fields = ('title', 'body_text')
