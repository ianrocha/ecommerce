import os
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from mimetypes import guess_type
from wsgiref.util import FileWrapper

from analytics.mixins import ObjectViewedMixin
from carts.models import Cart
from orders.models import ProductPurchase
from .models import Product, ProductFile


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        return Product.objects.all().featured()


class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
    template_name = 'products/featured-detail.html'

    def get_queryset(self):
        return Product.objects.features()


class UserProductHistoryView(LoginRequiredMixin, ListView):
    template_name = 'products/user-history.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProductHistoryView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        views = request.user.objectviewed_set.by_model(Product, model_queryset=False)
        return views


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()


class ProductDetailSlugView(ObjectViewedMixin, DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            return Http404('Not found.')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('Hummm...')

        # object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return instance


class ProductDownloadView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        pk = kwargs.get('pk')
        downloads_qs = ProductFile.objects.filter(pk=pk, product__slug=slug)
        if downloads_qs.count() != 1:
            raise Http404("Download not found")
        download_obj = downloads_qs.first()
        # permission checks
        can_download = False
        user_ready = True
        if download_obj.user_required:
            if request.user.is_authenticated:
                user_ready = False

        purchased_products = Product.objects.none()
        if download_obj.free:
            can_download = True
            user_ready = True
        else:
            purchased_products = ProductPurchase.objects.products_by_request(request)
            if download_obj.product in purchased_products:
                can_download = True

        if not can_download or not user_ready:
            messages.error(request, "You do not have access to download this item.")
            return redirect(download_obj.get_default_url())

        aws_file_path = download_obj.generate_download_url()
        return HttpResponseRedirect(aws_file_path)
        # file_root = settings.PROTECTED_ROOT
        # filepath = download_obj.file.path
        # final_filepath = os.path.join(file_root, filepath)
        # with open(final_filepath, 'rb') as f:
        #     wrapper = FileWrapper(f)
        #     mimetype = 'application/force-download'
        #     guessed_mimetype = guess_type(filepath)[0]
        #     if guessed_mimetype:
        #         mimetype = guessed_mimetype
        #     response = HttpResponse(wrapper, content_type=mimetype)
        #     response['Content-Disposition'] = 'attachment;filename={}'.format(download_obj.name)
        #     response['X-SendFile'] = str(download_obj.name)
        #     return response
        # return redirect(download_obj.get_absolut_url())


class ProductDetailView(ObjectViewedMixin, DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')

        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")

        return instance

    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)
