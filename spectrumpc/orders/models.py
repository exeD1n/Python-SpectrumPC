from django.db import models

class Computer(models.Model):
    name_droduct = models.CharField('Название', max_length=50)
    name_client = models.CharField('ФИО клиента', max_length=100)
    phone = models.CharField('Номер телефона пользователя', max_length=20)
    mail = models.CharField('Почта пользователя', max_length=50)
    addres = models.TextField('Место проживание')
    index_code = models.CharField('Почтовый индекс', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'