from django.shortcuts import render
from django.http import HttpRequest
from .forms import FeedbackForm
from homepage.views import ContextMixin


def index(request: HttpRequest):
    context = ContextMixin.context
    error = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Error'
    form = FeedbackForm()
    context.update({
        'feedback_form': form,
        'feedback_error': error
    })
    return render(request, 'customer/contact.html', context)
