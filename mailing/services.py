from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, MailingAttempt


def run_mailing(request, pk):
    """Функция запуска рассылки по требованию"""
    mailing = get_object_or_404(Mailing, id=pk)
    for recipient in mailing.recipients.all():
        try:
            mailing.status = Mailing.LAUNCHED
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.content,
                from_email=EMAIL_HOST_USER,
                recipient_list=[recipient.email],
                fail_silently=False,
            )
            MailingAttempt.objects.create(
                date_attempt=timezone.now(),
                status=MailingAttempt.STATUS_OK,
                server_response='Email отправлен',
                mailing=mailing,
            )
        except Exception as e:
            print(f"Ошибка при отправке письма для {recipient.email}: {str(e)}")
            MailingAttempt.objects.create(
                date_attempt=timezone.now(),
                status=MailingAttempt.STATUS_NOK,
                server_response=str(e),
                mailing=mailing,
            )
    if mailing.end_sending and mailing.end_sending <= timezone.now():
        # Если время рассылки закончилось, обновляем статус на "завершено"
        mailing.status = Mailing.COMPLETED
    mailing.save()
    return redirect('mailing:mailing_list')
