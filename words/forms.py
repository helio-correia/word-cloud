from django import forms

from .helpers import get_words_from_url
from .models import Word


class WebsiteForm(forms.Form):
    url = forms.URLField()

    def save(self):
        words = get_words_from_url(self.cleaned_data['url'])
        for word, count in words:
            obj, created = Word.objects.get_or_create(name=word, defaults={'count': 0})
            if created:
                obj.count = count
            else:
                obj.count += count
            obj.save()
