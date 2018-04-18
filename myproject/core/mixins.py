from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string


class EmailMixin:
    email_to = None
    email_context_name = None
    email_template_name = None
    email_from = settings.DEFAULT_FROM_EMAIL
    email_subject = ''

    def send_mail(self):
        """
        Método para envio de email seguindo padrão send_mail do Django.
        """
        subject = self.email_subject
        from_ = self.email_from
        to = self.get_email_to()
        template_name = self.get_email_template_name()
        context = self.get_email_context_data()
        body = render_to_string(template_name, context)
        return mail.send_mail(subject, body, from_, [to])

    def get_email_template_name(self):
        if self.email_template_name:
            return self.email_template_name
        return None

    def get_email_context_data(self):
        context = self.get_context_data()
        return context

    def get_email_to(self):
        email_to = self.request.POST.get('email_to')
        if email_to:
            return email_to
        return ''
