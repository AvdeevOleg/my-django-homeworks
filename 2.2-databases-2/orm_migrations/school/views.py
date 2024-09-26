from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    # Используем prefetch_related для уменьшения количества запросов
    students = Student.objects.prefetch_related('teachers').order_by('group')

    context = {
        'object_list': students  # передаем список учеников с их учителями
    }

    return render(request, template, context)
