from django.http import HttpRequest
from .forms import FeedbackForm
from homepage.views import ContextMixin
from django.views.generic import TemplateView

from catalog.models import Category


class ContactTemplateView(ContextMixin, TemplateView):
    template_name = 'customer/contact.html'

    def get_context_data(self):
        context = super(ContactTemplateView, self).get_context_data()
        context.update(self.context)
        context['feedback_form'] = FeedbackForm()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
