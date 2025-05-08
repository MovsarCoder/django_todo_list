from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from planner.models import Task
from django.db.models import Count


def tasks_list(request):
    tasks = Task.objects.select_related('category', 'priority').prefetch_related('tags').order_by('-created_at')

    # Подсчет выполненного количества задач

    done_count = Task.objects.filter(is_done=True).count()
    total = Task.objects.count()

    return render(request, 'index.html', context={
        'tasks': tasks,
        'done_count': done_count,
        'total': total
    })




