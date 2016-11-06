from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import CourseContact


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
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = CourseContact(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = CourseContact()
    else:
        form = CourseContact()

    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)
