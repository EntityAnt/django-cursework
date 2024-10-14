from django.contrib import admin

from mailing.models import RecipientMailing, Message, Mailing


@admin.register(RecipientMailing)
class RecipientMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email', 'comment',)
    list_filter = ('fio',)
    search_fields = ('fio', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'content',)
    search_fields = ('subject',)
    list_filter = ('subject',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_sending', 'end_sending', 'status', 'message',)
    search_fields = ('status',)
    list_filter = ('status',)
