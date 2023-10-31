from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from mail_distribution.forms import *
from mail_distribution.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index(request):
    context = {
        'mailing_list': MailDistribution.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'mail_distribution/index.html', context)


class MailDistributionListView(ListView):
    model = MailDistribution
    extra_context = {
        'title': 'Список рассылок'
    }


class MailDistributionDetailView(DetailView):
    model = MailDistribution


class MailDistributionCreateView(CreateView):
    model = MailDistribution
    form_class = MailDistributionForm
    success_url = reverse_lazy('mailings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.time_next = self.object.time_start
        if self.object.time_end <= self.object.time_next:
            self.object.status = constants.MAILING_FINISHED
        self.object.save()
        return super().form_valid(form)


class MailDistributionUpdateView(UpdateView):
    model = MailDistribution
    form_class = MailDistributionForm
    success_url = reverse_lazy('mailings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailDistributionDeleteView(DeleteView):
    model = MailDistribution
    success_url = reverse_lazy('mailings')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Список сообщений'
    }


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mail_list')


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients_list')
