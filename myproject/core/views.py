from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import EmailForm
from .mixins import EmailMixin


class Index(EmailMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        form = EmailForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        self.send_mail()
        return HttpResponseRedirect(reverse_lazy('core:index'))
