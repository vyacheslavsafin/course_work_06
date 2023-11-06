from django import forms

from mail_distribution.models import MailDistribution, Message, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailDistributionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailDistribution
        exclude = ('status', 'owner', 'time_next', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs.pop('initial').get('owner')
        self.fields['message'].queryset = Message.objects.all().filter(owner=user)
        self.fields['clients'].queryset = Client.objects.all().filter(owner=user)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)
