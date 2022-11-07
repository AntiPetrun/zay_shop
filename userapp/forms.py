from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import CharField, TextInput, PasswordInput, EmailInput


class SignUpForm(UserCreationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'type': 'text',
                'name': 'name',
                'id': 'name',
                'placeholder': 'Your Name'
            }
        ),
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'type': 'password',
                'name': 'pass',
                'id': 'pass',
                'placeholder': 'Enter Your Password'
            }
        ),
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'type': 'password',
                'name': 're_pass',
                'id': 're_pass',
                'placeholder': 'Repeat Your Password'
            }
        ),
    )
    email = CharField(
        widget=EmailInput(
            attrs={
                'type': 'email',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Your Email'
            }
        ),
    )


class SignInForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={
                'name': 'your_name',
                'id': 'your_name',
                'placeholder': 'Enter Your Username'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'your_pass',
                'id': 'your_pass',
                'placeholder': 'Enter Your Password'
            }
        )
    )
