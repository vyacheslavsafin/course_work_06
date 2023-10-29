from django.urls import path

from mail_distribution.views import *

urlpatterns = [
    path('', index, name='index'),
    path('mailings/', MailDistributionListView.as_view(), name='mailings'),
    path('<int:pk>/', MailDistributionDetailView.as_view(), name='mailing_detail'),
    path('create/', MailDistributionCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailDistributionUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailDistributionDeleteView.as_view(), name='mailing_delete'),

    path('mail_list/', MessageListView.as_view(), name='mail_list'),
    path('mail/<int:pk>/', MessageDetailView.as_view(), name='mail_detail'),
    path('mail_create/', MessageCreateView.as_view(), name='mail_create'),
    path('mail/update/<int:pk>', MessageUpdateView.as_view(), name='mail_update'),
    path('mail/delete/<int:pk>', MessageDeleteView.as_view(), name='mail_delete'),

    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
