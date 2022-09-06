from django.shortcuts import render, redirect
from . models import Order
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# can be used as one view two templates
@login_required
def place_order(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(id=pk)
        order_num = request.POST['order_num']
        Order.objects.create(book=book, user=get_user(request), num_order=order_num)
        messages.success(request, 'Order placed successfully')
        return redirect('place-order', pk)
    else:
        book = Book.objects.get(id=pk)
        # author = [a for a in book.author.all]
        orders= Order.objects.all()
        order = Order.objects.filter(user=get_user(request))
        user = get_user(request)
        context = {'orders':orders, "book":book,'order':order, 'user':user}
        # print(dir(request))
        return render(request, 'order/place-order/place-order.html', context)

# class PlaceOrder(DetailView):
#     model = Order
#     fields = '__all__'
#     template_name = 'order/place-order/place-order.html'
#     success_url = reverse_lazy('book-homepage')

def order_detail(request):
    order = Order.objects.filter(user=get_user(request))
    user = get_user(request)
    context = {'order':order, 'user':user}
    return render(request, 'order/order-detail/order-detail.html', context)
