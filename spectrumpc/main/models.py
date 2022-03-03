from django.db import models

# Create your models here.
class Mail(models.Model):
    mail = models.CharField('Почта пользователя', max_length=50)
    
    def __str__(self):
        return self.mail
    
    class Meta:
        verbose_name = 'Почта пользователя'
        verbose_name_plural = 'Почты пользователей'