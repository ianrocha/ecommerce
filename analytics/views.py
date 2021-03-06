import datetime
import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, View

from orders.models import Order


class SalesAjaxView(View):
    def get(self, request, *args, **kwargs):
        data = {}
        if request.user.is_staff:
            qs = Order.objects.all().by_weeks_range(weeks_ago=5, number_of_weeks=5)
            if request.GET.get('type') == 'week':
                days = 7
                start_date = timezone.now().today() - datetime.timedelta(days=days-1)
                datetime_list = [start_date + datetime.timedelta(days=x) for x in range(0, days)]

                labels = [day.strftime('%a') for day in datetime_list]

                sales_items = [qs.filter(updated__day=x.day, updated__month=x.month).totals_data()['total__sum'] or 0
                               for x in datetime_list]
                data['labels'] = labels
                data['data'] = sales_items
            elif request.GET.get('type') == '4weeks':
                data['labels'] = ['Four Weeks Ago', 'Three Weeks Ago', 'Two Weeks Ago', 'Last Week', 'This Week']
                data['data'] = [qs.by_weeks_range(weeks_ago=x, number_of_weeks=1).totals_data()['total__sum'] or 0
                                for x in range(5, -1, -1)]
        return JsonResponse(data)


class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, '400.html', {})
        return super(SalesView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SalesView, self).get_context_data(**kwargs)
        qs = Order.objects.all().by_weeks_range(weeks_ago=10, number_of_weeks=10)
        context['today'] = qs.by_range(start_date=timezone.now().date()).get_sales_breakdown()
        context['this_week'] = qs.by_weeks_range(weeks_ago=1, number_of_weeks=1).get_sales_breakdown()
        context['last_four_weeks'] = qs.by_weeks_range(weeks_ago=4, number_of_weeks=4).get_sales_breakdown()
        return context
