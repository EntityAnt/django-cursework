from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    RecipientMailingListView, RecipientMailingDetailView, RecipientMailingCreateView, RecipientMailingUpdateView, \
    RecipientMailingDeleteView, MessageDeleteView, MessageUpdateView, MessageCreateView, MessageDetailView, \
    MessageListView, IndexView

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/new/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('recipientmailing/', RecipientMailingListView.as_view(), name='recipientmailing_list'),
    path('recipientmailing/<int:pk>/detail/', RecipientMailingDetailView.as_view(), name='recipientmailing_detail'),
    path('recipientmailing/new/', RecipientMailingCreateView.as_view(), name='recipientmailing_create'),
    path('recipientmailing/<int:pk>/edit/', RecipientMailingUpdateView.as_view(), name='recipientmailing_update'),
    path('recipientmailing/<int:pk>/delete/', RecipientMailingDeleteView.as_view(), name='recipientmailing_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/detail/', MessageDetailView.as_view(), name='message_detail'),
    path('message/new/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
