from django.views.generic import ListView, DeleteView
from .models import Basket, OrderItem, Order
from catalog.models import Product, Category
from django.shortcuts import render
from homepage.views import ContextMixin
from django.urls import reverse_lazy


class AddToBasket(ContextMixin, ListView):
    template_name = 'order/basket.html'
    object_list = None
    model = OrderItem

    def get_context_data(self, **kwargs):
        context = super(AddToBasket, self).get_context_data(**kwargs)
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['user_profile'] = self.request.user
        return context

    def post(self, request, **kwargs):
        basket_id = self.request.session.get('basket')
        prod_uuid = self.request.POST.get('prod_uuid')

        if not basket_id:
            if self.request.user.is_anonymous:
                customer = None
            else:
                customer = self.request.user
            basket = Basket.objects.create(
                customer=customer
            )
            self.request.session['basket'] = basket.pk
        else:
            basket = Basket.objects.get(pk=basket_id)

        if prod_uuid:
            quantity = int(self.request.POST.get('quant'))
            product = Product.objects.get(article=prod_uuid)
            price = product.price * quantity
            prod_in_basket, created = OrderItem.objects.get_or_create(
                basket=basket,
                product=product,
                defaults={
                    'quantity': quantity,
                    'price': price
                },
            )

            if not created:
                prod_in_basket.quantity = prod_in_basket.quantity + quantity
                prod_in_basket.price = prod_in_basket.quantity * product.price
                prod_in_basket.save()

        context = super(AddToBasket, self).get_context_data(**kwargs)
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['user_profile'] = self.request.user
        context.update({
            'basket': basket,
        })
        return render(request, self.template_name, context)

    def get(self, request, **kwargs):
        basket_id = self.request.session.get('basket')
        basket = Basket.objects.get(pk=basket_id)
        context = super(AddToBasket, self).get_context_data(**kwargs)
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['user_profile'] = self.request.user
        context.update({
            'basket': basket,
        })
        return render(request, self.template_name, context)


class DeleteFromBasket(DeleteView):
    template_name = 'order/delete_from_basket.html'
    model = OrderItem
    success_url = reverse_lazy('order:add_to_basket')
