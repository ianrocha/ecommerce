from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchProductView, self).get_context_data(*kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self):
        """
        __icontains = field contains this
        __iexact = field is exactly this
        """
        request = self.request
        query = request.GET.get('q', None)

        if query:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.features()
        # return Product.objects.all()
