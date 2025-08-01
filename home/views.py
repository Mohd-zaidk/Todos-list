from django.shortcuts import render,HttpResponse
from home.models import Task
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
# Create your views here.

from django.shortcuts import render
from home.models import Task

def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        end_date = request.POST.get('end_date')
        is_completed = request.POST.get('is_completed') == 'on'  # ✅ checkbox returns "on"

        ins = Task(title=title, desc=desc, end_date=end_date, is_completed=is_completed)  # ✅ fixed
        ins.save()
        context['success'] = True
    return render(request, "index.html", context)


        
        #return HttpResponse("Form submitted successfully")
                             
    return render(request, "index.html", context)


from django.utils import timezone

from django.utils import timezone

def tasks(request):
    filter_type = request.GET.get('filter', 'all')

    if filter_type == 'pending':
        allTasks = Task.objects.filter(is_completed=False).order_by('end_date')
    elif filter_type == 'finished':
        allTasks = Task.objects.filter(is_completed=True).order_by('end_date')
    else:
        allTasks = Task.objects.all().order_by('end_date')

    context = {
        'tasks': allTasks,
        'filter': filter_type,
        'today': timezone.now().date()  # used for overdue highlighting
    }
    return render(request, "tasks.html", context)


def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('/tasks')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')

# UPDATE
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

