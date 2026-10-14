from django.shortcuts import redirect, render, get_object_or_404

from .form import TODOForm, updateTODO
from .models import TODO


def home(request):
    form = TODOForm()

    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    tasks = TODO.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def update(request, id):
    task = get_object_or_404(TODO, id=id)
    if request.method == 'POST':
        form = updateTODO(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = updateTODO(instance=task)

    return render(request, 'update.html', {'form': form})


def delete(request, id):
    task = get_object_or_404(TODO, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')