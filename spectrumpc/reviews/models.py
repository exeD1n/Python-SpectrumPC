from django.db import models


class reviews(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    reviews = models.TextField('Отзыв пользователя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'