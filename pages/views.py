from django.shortcuts import render

from .forms import WebsiteForm


def home(request):
    words = []
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            words = ['some', 'random', 'words']

    else:
        form = WebsiteForm()

    return render(request, 'pages/home.html', {'form': form, 'words': words})
