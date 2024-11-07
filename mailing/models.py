from django.db import models


class RecipientMailing(models.Model):
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)

    def __str__(self):
        return f"{self.fio} <{self.email}>"

    class Meta:
        verbose_name = "Получатель рассылки"
        verbose_name_plural = "Получатели рассылки"
        ordering = ["fio"]


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема сообщения")
    content = models.TextField(verbose_name="Содержание сообщения")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["subject"]


class Mailing(models.Model):
    CREATED = 'created'
    LAUNCHED = 'launched'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    first_sending = models.DateTimeField(verbose_name="Дата и время первого отправления")
    end_sending = models.DateTimeField(verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение", related_name="mailings")
    recipients = models.ManyToManyField(RecipientMailing, related_name="recipients", verbose_name="Получатели",
                                        help_text="Укажите получателей рассылки (используйте CTRL или COMMAND)")

    def __str__(self):
        return f"Рассылка {self.id}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["first_sending"]


class MailingAttempt(models.Model):
    date_attempt = models.DateTimeField(verbose_name="Дата и время попытки")
    status = models.CharField(max_length=15, verbose_name="Статус попытки")
    server_response = models.TextField(verbose_name="Ответ почтового сервера")
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка", related_name="mailing")

    def __str__(self):
        return f"{self.date_attempt} <{self.status}>"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ["date_attempt", "status"]
