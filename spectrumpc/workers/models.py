from django.db import models

# Create your models here.
class Work(models.Model):
    SHIRT_SIZES = (
        ('Д', 'Директор'),
        ('Т', 'Топ-Менеджер'),
        ('А', 'Администратор'),
        ('К', 'Консультант'),
        ('П', 'Продавец'),
    )
    name = models.TextField('ФИО')
    mesto = models.CharField('Место работы', max_length=100)
    doljonosti = models.CharField("Должность",max_length=1, choices=SHIRT_SIZES)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'