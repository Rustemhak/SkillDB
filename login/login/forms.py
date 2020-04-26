from django import forms
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _

# переопределил можно настраивать
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        max_length=254,
    )
    password = forms.CharField(
        max_length=60,
        min_length=6,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
