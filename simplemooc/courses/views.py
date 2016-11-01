from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    template_name = 'courses/index.html'
    context = {
        'courses': Course.objects.all()
    }
    return render(request, template_name, context)


# def details(request, pk):
#     template_name = 'courses/details.html'
#     context = {
#         'course': get_object_or_404(Course, pk=pk)
#     }
#     return render(request, template_name, context)

def details(request, slug):
    template_name = 'courses/details.html'
    context = {
        'course': get_object_or_404(Course, slug=slug)
    }
    return render(request, template_name, context)
