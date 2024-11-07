from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import MailingForm, RecipientForm, MessageForm
from mailing.models import Mailing, RecipientMailing, Message


class IndexView(TemplateView):
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'
        context_data['count_mailing'] = len(Mailing.objects.all())
        active_mailings_count = Mailing.objects.filter(status='launched').count()
        context_data['active_mailings_count'] = active_mailings_count
        unique_clients_count = RecipientMailing.objects.distinct().count()
        context_data['unique_clients_count'] = unique_clients_count
        return context_data


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = "Получатели"
        return context_data

    # def get_queryset(self, *args, **kwargs):
    #     if self.request.user.is_superuser or self.request.user.groups.filter(name='manager'):
    #         queryset = super().get_queryset()
    #     else:
    #         queryset = super().get_queryset().filter(owner=self.request.user)
    #     return queryset


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
