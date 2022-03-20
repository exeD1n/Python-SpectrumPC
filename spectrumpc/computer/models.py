from django.db import models


# Create your models here.
class Computer(models.Model):
    name = models.CharField('Название', max_length=50)
    img = models.ImageField('Фотография компьютера', upload_to='computer')
    title = models.CharField('Описание', max_length=250)
    CPU = models.CharField('Процессор', max_length=350)
    Cooling = models.CharField('Система охлаждения', max_length=350)
    Motherboard = models.CharField('Материнская плата', max_length=350)
    RAM = models.CharField('Оперативная память', max_length=350)
    GPU = models.CharField('Видеокарта', max_length=350)
    SSD = models.CharField('SSD', max_length=350)
    HDD = models.CharField('Жесткий диск', max_length=350)
    Power = models.CharField('Блок питания', max_length=350)
    Box = models.CharField('Корпус', max_length=350)
    Windows = models.CharField('Windows', max_length=350)
    Cost = models.CharField('Цена', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'


class Periferia(models.Model):
    name = models.CharField('Название', max_length=50)
    img = models.ImageField('Фотография переферии', upload_to='periferia')
    title = models.CharField('Описание', max_length=250)
    Cost = models.CharField('Цена', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Периферия'
        verbose_name_plural = 'Периферия'
