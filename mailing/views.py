from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Mailing, RecipientMailing, Message


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ['first_sending', 'end_sending', 'status', 'message']
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['first_sending', 'end_sending', 'status', 'message']
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class RecipientMailingListView(ListView):
    model = RecipientMailing


class RecipientMailingDetailView(DetailView):
    model = RecipientMailing


class RecipientMailingCreateView(CreateView):
    model = RecipientMailing
    fields = ['fio', 'email', 'comment']
    success_url = reverse_lazy('mailing:recipientmailing_list')


class RecipientMailingUpdateView(UpdateView):
    model = RecipientMailing
    fields = ['fio', 'email', 'comment']
    success_url = reverse_lazy('mailing:recipientmailing_list')


class RecipientMailingDeleteView(DeleteView):
    model = RecipientMailing
    success_url = reverse_lazy('mailing:recipientmailing_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'content']
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'content']
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
