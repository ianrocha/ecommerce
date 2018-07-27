from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'


def product_detail_view(request, pk=None, *args, **kwargs):
    queryset = get_object_or_404(Product, pk=pk)
    context = {
        'object': queryset
    }
    return render(request, 'products/detail.html', context)
