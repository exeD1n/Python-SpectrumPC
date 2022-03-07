from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'computer/product.html')

def computer(request):
    return render(request, 'computer/computer.html')

def periphery(request):
    return render(request, 'computer/periphery.html')