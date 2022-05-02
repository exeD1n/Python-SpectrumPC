from django.shortcuts import render, redirect
from .forms import OrderForm


# Create your views here.
def order(request):
    error = ""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            error = "Форма неверная"
    
    
    form = OrderForm()
    
    data = {
        'form' : form,
        'error' : error
    }
    
    return render(request, 'order/order.html', data)