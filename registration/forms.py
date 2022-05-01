from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponse
from users.models import CustomUser
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.error_messages['duplicate_username'] = 'Пользователь с таким E-MAIL уже существует'
        self.error_messages['duplicate_email'] = 'Пользователь с таким E-MAIL уже существует'

    # username = forms.CharField(label='Логин', required=True)
    first_name = forms.CharField(label='Имя', required=True,error_messages={
               'required': 'Пожалуйста введите своё имя',
                })
    email = forms.EmailField(required=True,error_messages={
               'required': 'Пожалуйста, введите свою эллектронную почту',
        'duplicate_username': "Пользователь с таким E-MAIL уже существует",
        'duplicate_email': "Пользователь с таким E-MAIL уже существует",
                })
    code = forms.CharField(required=False)
    password1 = forms.CharField(required=True, error_messages={
               'required': 'Придумайте пароль',})
    password2 = forms.CharField(required=True, error_messages={
        'required': 'Это обязательное поле', })
    error_messages = {
        'duplicate_username': "Пользователь с таким E-MAIL уже существует",
        'duplicate_email': "Пользователь с таким E-MAIL уже существует",
        'password_mismatch': "Введенные пароли не совпадают",
        'required':_("Это обязательное поле"),
    }

    field_order = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email, is_verificated=True).exists():
            raise forms.ValidationError("Пользователь с такой эллектронной почтой уже есть")
        return email.lower()
    class Meta:
        model = CustomUser
        fields = ('email',)
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Неправильный логин или пароль'
        super(LoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(
        label='email',
        required=True,
        error_messages={
            'required': 'Введите свою эллектронную почту'
        }
    )
    password = forms.CharField(
        label='password',
        required=True,
        error_messages={
            'required': 'Введите пароль от аккаунта Creplace'
        }
    )
    error_messages = {
        'required': _("Это обязательное поле"),
    }

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

