from .models import Order
from django.forms import ModelForm,TextInput,EmailInput

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name_client', 'name_droduct', 'phone', 'mail', 'addres', 'index_code', 'cost']
        
        widgets = {
            "name_client": TextInput(
                attrs={
                    "class":'form-control mb-3',
                    "placeholder": "Ваше ФИО"
                }                 
            ),
            "name_droduct": TextInput(
                attrs={
                    "class":'form-control mb-3',
                    "placeholder": "Название товара"
                }                 
            ),
            "phone": TextInput(
                attrs={
                    "class":'form-control mb-3',
                    "placeholder": "Ваш номер телефона"
                }                 
            ),
            'mail': EmailInput(
                attrs={
                    "class": 'form-control mb-3',
                    "placeholder": "name@example.com",
                }
            ),
            'addres': TextInput(
                attrs={
                    "class": 'form-control mb-3',
                    "placeholder": "Введите ваш адрес",
                }
            ),
            'index_code': TextInput(
                attrs={
                    "class": 'form-control mb-3',
                    "placeholder": "Введите ваш почтовый индекс",
                }
            ),
            'cost': TextInput(
                attrs={
                    "class": 'form-control',
                    "placeholder": "Цена товара",
                }
            ),
        }