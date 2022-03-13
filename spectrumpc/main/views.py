from django.shortcuts import redirect, render
from .forms import MailForm


# Create your views here.
def main(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = MailForm()
    data = {
        'form': form
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
