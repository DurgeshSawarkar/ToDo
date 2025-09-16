from django.shortcuts import redirect
from .models import Tasks

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Tasks.objects.create(task=task)
    return redirect('home')