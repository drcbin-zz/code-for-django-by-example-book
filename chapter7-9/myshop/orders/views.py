from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.get_discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],

                                        # 价格直接通过session来传递会不会有风险
                                        price = item['price'],
                                        quantity=item['quantity'])

            # clear the cart
            cart.clear()

            # launch the asyncronous task to send a email
            order_created.delay(order.id)
            # return render(request, 'orders/order/created.html', {'order': order})  # deleted in chapter 8

            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))   # redirect to the payment

    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})
