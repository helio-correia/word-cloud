from django.shortcuts import render

from words.helpers import get_words_from_url
from words.forms import WebsiteForm


def home(request):
    words = []
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            words = get_words_from_url(form.cleaned_data['url'])
            form.save()
    else:
        form = WebsiteForm()

    return render(request, 'pages/home.html', {'form': form, 'words': words})


def login(request):
    return render(request, 'pages/login.html')


def admin(request):
    return render(request, 'pages/admin.html')
