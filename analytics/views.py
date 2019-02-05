from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Sum
from django.shortcuts import render
from django.views.generic import TemplateView

from orders.models import Order


class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, '400.html', {})
        return super(SalesView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SalesView, self).get_context_data(**kwargs)
        qs = Order.objects.all()
        context['orders'] = qs
        context['recent_orders'] = qs.recent().not_refunded()[:5]
        context['recent_orders_data'] = context['recent_orders'].totals_data()
        context['recent_orders_cart_data'] = context['recent_orders'].cart_data()
        context['shipped_orders'] = qs.recent().not_refunded().by_status(status='shipped')[:5]
        context['shipped_orders_data'] = context['shipped_orders'].totals_data()
        context['paid_orders'] = qs.recent().not_refunded().by_status(status='paid')[:5]
        context['paid_orders_data'] = context['paid_orders'].totals_data()
        return context
