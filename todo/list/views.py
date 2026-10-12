from django.shortcuts import render

from .models import TODO


def home(request):
    task = TODO.objects.all()
    return render(request, 'home.html', {'task': task})
