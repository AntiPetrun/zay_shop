from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'name': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control mt-1',
                    'id': 'name',
                    'name': 'name',
                    'placeholder': 'Name',
                }
            ),
            'email': EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control mt-1',
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Email',
                }
            ),
            'subject': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control mt-1',
                    'id': 'subject',
                    'name': 'subject',
                    'placeholder': 'Subject',
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control mt-1',
                    'id': 'message',
                    'name': 'message',
                    'placeholder': 'Message',
                    'rows': '8'
                }
            )
        }
