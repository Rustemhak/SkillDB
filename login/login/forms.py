from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


# переопределил можно настраивать
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        max_length=254,
    )
    password = forms.CharField(
        max_length=60,
    )
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }


class PasswordResetEmailForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetEmailForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        max_length=254,
    )

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        email = self.cleaned_data["email"]
        email_field_name = UserModel.get_email_field_name()
        if email.endswith('@stud.kpfu.ru'):
            for user in self.get_users(email):
                if not domain_override:
                    current_site = get_current_site(request)
                    site_name = current_site.name
                    domain = current_site.domain
                else:
                    site_name = domain = domain_override
                user_email = getattr(user, email_field_name)
                context = {
                    'email': user_email,
                    'domain': domain,
                    'site_name': site_name,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': token_generator.make_token(user),
                    'protocol': 'https' if use_https else 'http',
                    **(extra_email_context or {}),
                }
                self.send_mail(
                    subject_template_name, email_template_name, context, from_email,
                    user_email, html_email_template_name=html_email_template_name,
                )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=20,
    )
    new_password2 = forms.CharField(
        max_length=20,
    )
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

