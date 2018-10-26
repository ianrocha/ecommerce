from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.shortcuts import render, redirect

from .forms import MarketingPreferenceForm
from .models import MarketingPreference


class MarketingPreferenceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MarketingPreferenceForm
    template_name = 'base/forms.html'
    success_url = '/settings/email/'
    success_message = 'Your email preferences have been updated. Thank You!'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('/login/?next=/settings/email/')  # HttpResponse('Not Allowed', status=400)
        return super(MarketingPreferenceUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MarketingPreferenceUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Email Preferences'
        return context

    def get_object(self, queryset=None):
        user = self.request.user
        obj, created = MarketingPreference.objects.get_or_create(user=user)
        return obj
