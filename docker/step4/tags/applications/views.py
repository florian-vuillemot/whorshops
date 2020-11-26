from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Application as ApplicationModel
from .forms import ApplicationForm


class Application(ListView):
    model = ApplicationModel
    template_name = 'applications/all.html'


class NewApplication(CreateView):
    model = ApplicationModel
    form_class = ApplicationForm
    template_name = 'applications/new.html'
    success_url = reverse_lazy('applications:all')
