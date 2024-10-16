from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm
from meals.models import Meals
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()
    

class OrdersDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'  
    context_object_name = 'meal'
    

@method_decorator(login_required, name='dispatch')  
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_order.html'
    success_url = '/orders/'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=1)
        context['formset'] = OrderItemFormSet(queryset=OrderItem.objects.none())
        return context

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user  
        order.save()

        total_price = 0
        OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm)
        formset = OrderItemFormSet(self.request.POST)

        if formset.is_valid():
            for order_item_form in formset:
                order_item = order_item_form.save(commit=False)
                order_item.order = order
                order_item.save()
                total_price += order_item.meal.price * order_item.quantity

           
            order.total_price = total_price
            order.save()
            return redirect(self.success_url)
        else:
            
            context = self.get_context_data(form=form)
            context['formset'] = formset
            return self.render_to_response(context)



@method_decorator(login_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_update.html'
    success_url = '/orders/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=0) 
        order = self.get_object() 
        context['formset'] = OrderItemFormSet(queryset=OrderItem.objects.filter(order=order)) 
        return context

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user  
        order.save()

        total_price = 0
        OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm)
        formset = OrderItemFormSet(self.request.POST, queryset=OrderItem.objects.filter(order=order))

        if formset.is_valid():
            for order_item_form in formset:
                order_item = order_item_form.save(commit=False)
                order_item.order = order  
                order_item.save() 

                total_price += order_item.meal.price * order_item.quantity 

            order.total_price = total_price
            order.save()
            return redirect(self.success_url)
        else:
            
            context = self.get_context_data(form=form)
            context['formset'] = formset
            return self.render_to_response(context)




class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_delete.html'  
    success_url = reverse_lazy('order_list')
