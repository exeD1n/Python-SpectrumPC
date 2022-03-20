from django.shortcuts import render
from .models import Periferia, Computer
from django.views.generic import DetailView


def product(request):
    return render(request, 'computer/product.html')


def computer(request):
    computer = Computer.objects.all()
    return render(request, 'computer/computer.html', {'computer': computer})


class ComputerDetailView(DetailView):
    model = Computer
    template_name = 'computer/computer_detail.html'
    context_object_name = 'computer'


def periphery(request):
    periferia = Periferia.objects.all()
    return render(request, 'computer/periphery.html', {'periferia': periferia})
