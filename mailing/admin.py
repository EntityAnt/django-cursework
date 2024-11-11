from django.contrib import admin

from mailing.models import RecipientMailing, Message, Mailing
from users.models import User


@admin.register(RecipientMailing)
class RecipientMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email', 'comment', 'owner')
    list_filter = ('fio',)
    search_fields = ('fio', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'content', 'owner',)
    search_fields = ('subject',)
    list_filter = ('subject',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_sending', 'end_sending', 'status', 'message', 'owner')
    search_fields = ('status',)
    list_filter = ('status',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number', )
    search_fields = ('email',)
    list_filter = ('email',)
