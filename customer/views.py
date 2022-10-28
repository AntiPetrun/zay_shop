from django.shortcuts import render
from django.http import HttpRequest
from .forms import FeedbackForm


def index(request: HttpRequest):
    error = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Error'
    form = FeedbackForm()
    return render(
        request,
        'customer/contact.html',
        {'feedback_form': form, 'feedback_error': error}
    )
