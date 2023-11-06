from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from mail_distribution.forms import *
from mail_distribution.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mail_distribution.utils import counters


@login_required
def index(request):
    context = counters()
    return render(request, 'mail_distribution/index.html', context)


class MailDistributionListView(LoginRequiredMixin, ListView):
    model = MailDistribution
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        if not self.request.user.is_staff:
            return MailDistribution.objects.filter(owner=self.request.user)
        else:
            return MailDistribution.objects.all()


class MailDistributionDetailView(LoginRequiredMixin, DetailView):
    model = MailDistribution


class MailDistributionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def test_func(self):
        return not self.request.user.is_staff

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial


class MailDistributionUpdateView(LoginRequiredMixin, UpdateView):
    model = MailDistribution
    form_class = MailDistributionForm
    success_url = reverse_lazy('mailings')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailDistributionDeleteView(LoginRequiredMixin, DeleteView):
    model = MailDistribution
    success_url = reverse_lazy('mailings')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Список сообщений'
    }

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Message.objects.filter(owner=self.request.user)
        else:
            return Message.objects.all()


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mail_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов'
    }

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Client.objects.filter(owner=self.request.user)
        else:
            return Client.objects.all()


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients_list')


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs
    extra_context = {
        'title': 'Логи'
    }

    def get_queryset(self):
        return Logs.objects.filter(owner=self.request.user)


@login_required
def toggle_activity(request, pk):
    if request.user.is_staff:
        mailing = get_object_or_404(MailDistribution, pk=pk)
        if mailing.is_active:
            mailing.is_active = False
        else:
            mailing.is_active = True
        mailing.save()
    return redirect(reverse('mailings'))
