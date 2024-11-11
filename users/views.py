import secrets

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm, UserLoginForm, PasswordRecoveryForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:email_confirmation')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        user.token = token
        user.save()
        send_mail(
            subject='Подтверждение почты',
            message=f'Здравствуйте, перейдите по ссылке для подтверждения почты: {url} ',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UserLoginView(LoginView):
    model = User
    form_class = UserLoginForm


class EmailConfirmationView(TemplateView):
    model = User
    template_name = 'users/email_confirmation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class PasswordRecoveryView(FormView):
    template_name = 'users/password_recovery.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:reset_password')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)  # Получаем пользователя по email
        user.is_active = False  # Делаем пользователя неактивным
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        user.token = token
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message=f'Здравствуйте, перейдите по ссылке для восстановление пароля: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)