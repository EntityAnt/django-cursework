from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingForm, RecipientForm, MessageForm
from mailing.models import Mailing, RecipientMailing, Message


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing
    form_class = MailingForm


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class RecipientMailingListView(ListView):
    model = RecipientMailing


class RecipientMailingDetailView(DetailView):
    model = RecipientMailing
    form_class = RecipientForm


class RecipientMailingCreateView(CreateView):
    model = RecipientMailing
    form_class = RecipientForm
    success_url = reverse_lazy('mailing:recipientmailing_list')


class RecipientMailingUpdateView(UpdateView):
    model = RecipientMailing
    form_class = RecipientForm
    success_url = reverse_lazy('mailing:recipientmailing_list')


class RecipientMailingDeleteView(DeleteView):
    model = RecipientMailing
    success_url = reverse_lazy('mailing:recipientmailing_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message
    form_class = MessageForm


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
