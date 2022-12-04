from django import forms
from django.core.exceptions import ValidationError
import re
from .logic import file_remove


class EnterURL(forms.Form):
    urls = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'textarea33', 'placeholder': '複数のURLは改行して入力'}),
        required=False)

    def clean(self):
        data = super().clean()
        file_remove()
        print(f'>>>data  {data}')

        if not data['urls']:
            raise ValidationError("URLを入力してください")
        urls = data['urls'].split()
        for url in urls:
            if not re.match("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", url):
                raise ValidationError("URLではない入力値が存在しています")
        if len(urls) > 10:
            raise ValidationError("同時に処理できるURLは10個までです")

        return urls
